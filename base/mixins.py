from django.db.models import Model
from typing import Any, Dict
from django.urls import reverse
from django.core.cache import cache
from django.views.generic import TemplateView


class ModelContextMixin:
    model: Model = None
    paginate_by = 10

    def get_queryset(self):
        queryset_cache_key = f'{self.model.__name__}_queryset'
        queryset = cache.get(queryset_cache_key)

        if queryset is None:
            queryset = self.model.objects.all().select_related()
            cache.set(queryset_cache_key, queryset)
        
        orderby = self.request.GET.get('orderby', None)
        if orderby:
            queryset = queryset.order_by(orderby)

        return queryset

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        model = self.model

        if model:
            fields_cache_key = f'{model.__name__}_fields'
            fields = cache.get(fields_cache_key)
            
            if fields is None:
                fields = [field for field in model._meta.fields]
                cache.set(fields_cache_key, fields)

            context['fields'] = fields
            context['model_name'] = model._meta.verbose_name_plural
        
        return context


class ModelFormMixin:
    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()

        form = self.get_form()
        if form.is_valid():
            form.save()
            queryset_cache_key = f'{self.model.__name__}_queryset'
            cache.delete(queryset_cache_key)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        

class ModelSuccessUrlMixin:
    def get_success_url(self):
        model_name = self.model.__name__.lower()
        return reverse(f"{model_name}_list")