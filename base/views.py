from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from .mixins import ModelContextMixin, ModelSuccessUrlMixin
from .forms import DynamicModelForm
from .models import Book, Author, Genre, OrderItem, Bill

class HomeView(generic.TemplateView):
    template_name = 'base/home.html'


class BookView(ModelContextMixin, ModelSuccessUrlMixin, generic.edit.FormMixin, generic.ListView):
    model = Book
    template_name = 'base/books.html'
    context_object_name = 'books'
    form_class = DynamicModelForm.create(Book)
    extra_context = {'add_button_name': 'Додати нову книгу'}


class AuthorView(ModelContextMixin, ModelSuccessUrlMixin, generic.edit.FormMixin, generic.ListView):
    model = Author
    template_name = 'base/authors.html'
    form_class = DynamicModelForm.create(Author)
    extra_context = {'add_button_name': 'Додати нового автора'}


class GenreView(ModelContextMixin, ModelSuccessUrlMixin, generic.edit.FormMixin, generic.ListView):
    model = Genre
    template_name = 'base/genres.html'
    form_class = DynamicModelForm.create(Genre)
    extra_context = {'add_button_name': 'Додати новий жанр'}


class OrderItemView(ModelContextMixin, ModelSuccessUrlMixin, generic.edit.FormMixin, generic.ListView):
    model = OrderItem
    template_name = 'base/orders.html'
    form_class = DynamicModelForm.create(OrderItem)
    extra_context = {'add_button_name': 'Додати новий товар'}


class BillView(ModelContextMixin, ModelSuccessUrlMixin, generic.edit.FormMixin, generic.ListView):
    model = Bill
    template_name = 'base/bills.html'
    form_class = DynamicModelForm.create(Bill)
    extra_context = {'add_button_name': 'Додати новий чек'}
