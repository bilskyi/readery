from typing import Type
from django import forms
from django.forms import ModelForm
from .models import Book, Author, Genre, OrderItem, Bill

# Generic ModelForm that takes a model as a parameter
class DynamicModelForm(ModelForm):
    class Meta:
        model = None  # Placeholder, to be set in subclasses
        fields = '__all__'  # Use all fields by default

    @classmethod
    def create(cls, _model: Type):
        # Dynamically create a form for the specified model
        class Meta(cls.Meta):
            model = _model
        
        # Create a new form class with the specified model
        form_class = type(f"{_model.__name__}Form", (cls,), {'Meta': Meta})
        return form_class
