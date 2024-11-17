from typing import Type
from django import forms
from django.forms import ModelForm
from .models import Book, Author, Genre, OrderItem, Bill
from django.utils.timezone import now


class DynamicModelForm(ModelForm):
    class Meta:
        model = None
        fields = '__all__'

    @classmethod
    def create(cls, _model: Type):
        class Meta(cls.Meta):
            model = _model
    

        form_class = type(f"{_model.__name__}Form", (cls,), {'Meta': Meta})
        return form_class
    

class OrderItemForm(DynamicModelForm.create(OrderItem)):
    price = forms.DecimalField(
        max_digits=5,
        decimal_places=2,
        label='Ціна',
        required=False,
        disabled=True
    )

    bill = forms.ModelChoiceField(queryset=Bill.objects.all(), required=False, label='', widget=forms.HiddenInput())

    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data.get('quantity')
        book = cleaned_data.get('book')

        if book and quantity:
            cleaned_data['price'] = book.price * quantity
        else:
            cleaned_data['price'] = 0

        bill = cleaned_data.get('bill')
        
        if not bill:
            bill = Bill.objects.create(date=now(), total_amount=0.00)
            cleaned_data['bill'] = bill

        return cleaned_data