from django.urls import path
from django.views.generic.base import RedirectView
from .views import *
from . import utils

urlpatterns = [
    # Home URL
    path('', RedirectView.as_view(url='books/', permanent=True)),

    # Book URLs
    path('books/', BookView.as_view(), name='book_list'),
    path('books/update/<slug:slug>/', UpdateBookView.as_view(), name='update_book'),
    path('books/delete/<slug:slug>/', DeleteBookView.as_view(), name='book_delete'),


    # Author URLs
    path('authors/', AuthorView.as_view(), name='author_list'),
    path('authors/update/<slug:slug>/', UpdateAuthorView.as_view(), name='update_author'),
    path('authors/delete/<slug:slug>/', DeleteAuthorView.as_view(), name='author_delete'),

    # Genre URLs
    path('genres/', GenreView.as_view(), name='genre_list'),
    path('genres/update/<slug:slug>/', UpdateGenreView.as_view(), name='update_genre'),
    path('genres/delete/<slug:slug>/', DeleteGenreView.as_view(), name='genre_delete'),

    # OrderItem URLs
    path('orders/', OrderItemView.as_view(), name='orderitem_list'),
    path('orders/update/<int:pk>/', UpdateOrderItemView.as_view(), name='update_orderitem'),
    path('orders/delete/<int:pk>/', DeleteOrderItemView.as_view(), name='orderitem_delete'),

    # Bill URLs
    path('bills/', BillView.as_view(), name='bill_list'),
    path('bills/update/<int:pk>/', UpdateBillView.as_view(), name='update_bill'),
    path('bills/delete/<int:pk>/', DeleteBillView.as_view(), name='bill_delete'),


    # JSON resopnses
    path('books/<int:book_id>/price/', utils.get_book_price, name='get_book_price'),
]