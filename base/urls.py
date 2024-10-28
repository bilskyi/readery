from django.urls import path
from .views import *

urlpatterns = [
    path('', BookView.as_view(), name='book_list'),
    path('authors/', AuthorView.as_view(), name='author_list'),
    path('genres/', GenreView.as_view(), name='genre_list'),
    path('orders/', OrderItemView.as_view(), name='orderitem_list'),
    path('bills/', BillView.as_view(), name='bill_list'),
]