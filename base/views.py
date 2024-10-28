from typing import Any
from django.shortcuts import render
from django.views import generic
from .mixins import ModelContextMixin
from .models import Book, Author, Genre, OrderItem, Bill



class HomeView(generic.TemplateView):
    template_name = 'base/home.html'
    

class BookView(ModelContextMixin, generic.ListView):
    model = Book
    template_name = 'base/home.html'


class AuthorView(ModelContextMixin, generic.ListView):
    model = Author
    template_name = 'base/authors.html'


class GenreView(ModelContextMixin, generic.ListView):
    model = Genre
    template_name = 'base/genres.html'


class OrderItemView(ModelContextMixin, generic.ListView):
    model = OrderItem
    template_name = 'base/orders.html'


class BillView(ModelContextMixin, generic.ListView):
    model = Bill
    template_name = 'base/bills.html'
