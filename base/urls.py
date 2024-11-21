from django.urls import path
from django.views.generic.base import RedirectView
from .views import *
from . import utils

urlpatterns = [
    # Home URL
    path('', RedirectView.as_view(url='books/', permanent=True)),
    path('search/', SearchView.as_view(), name='search'),


    # Book URLs
    path('books/', BookView.as_view(), name='book_list'),
    path('books/update/<slug:slug>/', UpdateBookView.as_view(), name='update_book'),
    path('books/delete/<slug:slug>/', DeleteBookView.as_view(), name='delete_book'),


    # Author URLs
    path('authors/', AuthorView.as_view(), name='author_list'),
    path('authors/update/<slug:slug>/', UpdateAuthorView.as_view(), name='update_author'),
    path('authors/delete/<slug:slug>/', DeleteAuthorView.as_view(), name='delete_author'),

    # Genre URLs
    path('genres/', GenreView.as_view(), name='genre_list'),
    path('genres/update/<slug:slug>/', UpdateGenreView.as_view(), name='update_genre'),
    path('genres/delete/<slug:slug>/', DeleteGenreView.as_view(), name='delete_genre'),

    # OrderItem URLs
    path('orders/', OrderItemView.as_view(), name='orderitem_list'),
    path('orders/update/<int:pk>/', UpdateOrderItemView.as_view(), name='update_orderitem'),
    path('orders/delete/<int:pk>/', DeleteOrderItemView.as_view(), name='delete_orderitem'),

    # Bill URLs
    path('bills/', BillView.as_view(), name='bill_list'),
    path('bills/update/<int:pk>/', UpdateBillView.as_view(), name='update_bill'),
    path('bills/delete/<int:pk>/', DeleteBillView.as_view(), name='delete_bill'),


    # JSON resopnses
    path('books/<int:book_id>/price/', utils.get_book_price, name='get_book_price'),
    path('export/<str:model_name>', utils.export_table_to_excel, name='export_table_to_excel'),
]