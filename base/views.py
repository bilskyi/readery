from typing import Any
from django.shortcuts import render
from django.views import generic
from .mixins import ModelFieldsContextMixin
from .models import Book, Author, Genre, OrderItem, Bill


class HomeView(generic.TemplateView):
    template_name = 'base/home.html'
    

class BookView(ModelFieldsContextMixin, generic.ListView):
    model = Book
    template_name = 'base/home.html'


class AuthorView(ModelFieldsContextMixin, generic.ListView):
    model = Author
    template_name = 'base/authors.html'


class GenreView(ModelFieldsContextMixin, generic.ListView):
    model = Genre
    template_name = 'base/genres.html'


class OrderItemView(ModelFieldsContextMixin, generic.ListView):
    model = OrderItem
    template_name = 'base/orders.html'


class BillView(ModelFieldsContextMixin, generic.ListView):
    model = Bill
    template_name = 'base/bills.html'
