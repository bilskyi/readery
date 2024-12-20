from django.shortcuts import redirect, render
from django.core.cache import cache
from django.db.models import Prefetch
from django.views import View, generic
from watson import search as watson_search
from .mixins import ModelContextMixin, ModelSuccessUrlMixin, ModelFormMixin
from .forms import DynamicModelForm, OrderItemForm, OrderItemFormSet
from .models import Book, Author, Genre, OrderItem, Bill
from django.core.paginator import Paginator
from django.utils.timezone import now


class HomeView(generic.TemplateView):
    template_name = 'base/home.html'


class BookView(ModelContextMixin, ModelFormMixin, ModelSuccessUrlMixin, generic.edit.FormMixin, generic.ListView):
    model = Book
    template_name = 'base/books.html'
    form_class = DynamicModelForm.create(Book)
    extra_context = {'add_button_name': 'Додати нову книгу'}


class AuthorView(ModelContextMixin, ModelFormMixin, ModelSuccessUrlMixin, generic.edit.FormMixin, generic.ListView):
    model = Author
    template_name = 'base/authors.html'
    form_class = DynamicModelForm.create(Author)
    extra_context = {'add_button_name': 'Додати нового автора'}


class GenreView(ModelContextMixin, ModelFormMixin, ModelSuccessUrlMixin, generic.edit.FormMixin, generic.ListView):
    model = Genre
    template_name = 'base/genres.html'
    form_class = DynamicModelForm.create(Genre)
    extra_context = {'add_button_name': 'Додати новий жанр'}


class OrderItemView(ModelContextMixin, ModelFormMixin, ModelSuccessUrlMixin, generic.edit.FormMixin, generic.ListView):
    model = OrderItem
    template_name = 'base/orders.html'
    form_class = OrderItemForm
    extra_context = {'add_button_name': 'Додати новий товар'}

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['orderitem_formset'] = OrderItemFormSet(queryset=OrderItem.objects.filter(bill=None))
        return context

    def post(self, request, *args, **kwargs):
        context = super().post(request, *args, **kwargs)
        bill = Bill.objects.create(date=now(), total_amount=0.00)  # You can customize this as needed

        # Handle the formset
        formset = OrderItemFormSet(request.POST)

        if formset.is_valid():
            for form in formset:
                order_item = form.save(commit=False)
                order_item.bill = bill
                order_item.save()

            # Invalidate queryset cache after modifying the data
            queryset_cache_key = f'{self.model.__name__}_queryset'
            cache.delete(queryset_cache_key)

            return redirect('orderitem_list')

        context = self.get_context_data()
        context['orderitem_formset'] = formset
        return self.render_to_response(context)

class BillView(ModelContextMixin, ModelFormMixin, ModelSuccessUrlMixin, generic.edit.FormMixin, generic.ListView):
    model = Bill
    template_name = 'base/bills.html'
    form_class = DynamicModelForm.create(Bill)
    extra_context = {'add_button_name': 'Додати новий чек'}

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        # Getting the list of bills with prefetching
        bills = self.get_queryset().prefetch_related(
            Prefetch('orderitem_set', queryset=OrderItem.objects.select_related('book')),
        )

        # Pagination logic
        paginator = Paginator(bills, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        # Add the page object to the context to render pagination links in the template
        context['page_obj'] = page_obj
        context['bills'] = page_obj.object_list
        
        return context

class BaseUpdateView(ModelFormMixin, ModelSuccessUrlMixin, generic.UpdateView):
    template_name = 'base/update.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        return super().post(request, *args, **kwargs)


class UpdateBookView(BaseUpdateView):
    model = Book
    form_class = DynamicModelForm.create(Book)


class UpdateAuthorView(BaseUpdateView):
    model = Author
    form_class = DynamicModelForm.create(Author)


class UpdateGenreView(BaseUpdateView):
    model = Genre
    form_class = DynamicModelForm.create(Genre)


class UpdateOrderItemView(BaseUpdateView):
    model = OrderItem
    form_class = DynamicModelForm.create(OrderItem)


class UpdateBillView(BaseUpdateView):
    model = Bill
    form_class = DynamicModelForm.create(Bill)


class BaseDeleteView(ModelSuccessUrlMixin, generic.DeleteView):
    template_name = 'base/delete.html'

    def post(self, request, *args, **kwargs):
        model_name = self.model.__name__
        queryset_cache_key = f'{model_name}_queryset'
        
        response = super().post(request, *args, **kwargs)
        
        cache.delete(queryset_cache_key)
        
        return response
    

class DeleteBookView(BaseDeleteView):
    model = Book


class DeleteAuthorView(BaseDeleteView):
    model = Author


class DeleteGenreView(BaseDeleteView):
    model = Genre


class DeleteOrderItemView(BaseDeleteView):
    model = OrderItem


class DeleteBillView(BaseDeleteView):
    model = Bill
    

class SearchView(View):
    template_name = 'base/search_results.html'

    def get(self, request):
        query = request.GET.get('query', '')
        results = []
        
        if query:
            search_results = watson_search.search(query)

            for result in search_results:
                if result.object:
                    fields = {
                        field.verbose_name: getattr(result.object, field.name, '')
                        for field in result.object._meta.fields
                    }

                    results.append({
                        'obj': result.object,
                        'fields': fields,
                        'model_name': result.object._meta.verbose_name,
                    })
                else:
                    continue

        return render(request, self.template_name, {
            'query': query,
            'results': results,
        })