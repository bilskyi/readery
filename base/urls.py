from django.urls import path
from django.views.generic.base import RedirectView
from .views import *
from . import utils

urlpatterns = [
    path('', RedirectView.as_view(url='books/', permanent=True)),
    path('books/', BookView.as_view(), name='book_list'),
    path('authors/', AuthorView.as_view(), name='author_list'),
    path('genres/', GenreView.as_view(), name='genre_list'),
    path('orders/', OrderItemView.as_view(), name='orderitem_list'),
    path('bills/', BillView.as_view(), name='bill_list'),

    # JSON resopnses
    path('books/<int:book_id>/price/', utils.get_book_price, name='get_book_price'),
]