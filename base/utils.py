import openpyxl
from openpyxl.styles import Font
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Book, Author
from django.apps import apps
from django.views import View


def get_book_price(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        return JsonResponse({'price': book.price})
    except Book.DoesNotExist:
        return JsonResponse({'error': 'Book not found'}, status=404)


from django.apps import apps
from django.http import HttpResponse
from openpyxl import Workbook
from openpyxl.styles import Font

def export_table_to_excel(request, model_name=None):
    try:
        model = apps.get_model(app_label="base", model_name=model_name)
    except LookupError:
        return HttpResponse("Invalid model name", status=400)

    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = "Data Export"

    fields = [field.name for field in model._meta.fields]
    field_verbose_names = [field.verbose_name for field in model._meta.fields]

    worksheet.append(field_verbose_names)

    for cell in worksheet[1]:
        cell.font = Font(bold=True)

    for obj in model.objects.all():
        row = []
        for field in fields:
            value = getattr(obj, field, "")
            if hasattr(value, "__str__"):
                value = str(value)
            row.append(value)
        worksheet.append(row)

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = f'attachment; filename="{model.__name__}.xlsx"'

    workbook.save(response)
    return response
