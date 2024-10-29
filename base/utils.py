from django.http import JsonResponse
from .models import Book

def get_book_price(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        return JsonResponse({'price': book.price})
    except Book.DoesNotExist:
        return JsonResponse({'error': 'Book not found'}, status=404)
