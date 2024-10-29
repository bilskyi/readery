from typing import Type
from django import forms
from django.forms import ModelForm
from .models import Book, Author, Genre, OrderItem, Bill


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
