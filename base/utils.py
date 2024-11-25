import openpyxl
from openpyxl.styles import Font
from django.http import HttpResponse
from django.http import JsonResponse
from weasyprint import HTML
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Book, Bill
from django.apps import apps
from django.views import View


def get_book_price(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        return JsonResponse({'price': book.price})
    except Book.DoesNotExist:
        return JsonResponse({'error': 'Book not found'}, status=404)
    

def export_table_to_excel(request, model_name=None):
    try:
        model = apps.get_model(app_label="base", model_name=model_name)
    except LookupError:
        return HttpResponse("Invalid model name", status=400)

    workbook = openpyxl.Workbook()
    worksheet = workbook.active
    worksheet.title = f"{model.__name__} Data"

    fields = [field.name for field in model._meta.fields]
    field_verbose_names = [field.verbose_name for field in model._meta.fields]

    if model_name.lower() == "bill":
        fields.append("ordered_goods")
        field_verbose_names.append("Ordered Goods")

    worksheet.append(field_verbose_names)

    for cell in worksheet[1]:
        cell.font = Font(bold=True)

    for obj in model.objects.all():
        row = []
        for field in fields:
            if field == "ordered_goods" and hasattr(obj, "orderitem_set"):
                ordered_goods = ", ".join(
                    [
                        f"{item.book.title} - {item.quantity} x {item.book.price} грн"
                        for item in obj.orderitem_set.all()
                    ]
                )
                row.append(ordered_goods)
            else:
                value = getattr(obj, field, "")
                if hasattr(value, "__str__"):
                    value = str(value)
                row.append(value)
        worksheet.append(row)

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = f'attachment; filename="export_{model.__name__}.xlsx"'

    workbook.save(response)
    return response


def export_bill_to_pdf(request, pk):
    # Fetch the Bill and related order items
    bill = get_object_or_404(Bill, pk=pk)
    order_items = bill.orderitem_set.select_related('book')
    
    # Render the HTML template
    html_string = render_to_string('pdf_templates/bill.html', {'bill': bill, 'order_items': order_items})
    
    # Generate the PDF
    pdf = HTML(string=html_string).write_pdf()

    # Return as a downloadable response
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="bill_{bill.pk}.pdf"'
    return response