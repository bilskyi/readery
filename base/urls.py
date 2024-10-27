from django.urls import path
from .views import *

urlpatterns = [
    path('', BookView.as_view(), name='books'),
    path('authors/', AuthorView.as_view(), name='authors'),
    path('genres/', GenreView.as_view(), name='genres'),
    path('orders/', OrderItemView.as_view(), name='orders'),
    path('bills/', BillView.as_view(), name='bills'),
]