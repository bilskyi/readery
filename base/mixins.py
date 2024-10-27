from django.db.models import Model
from typing import Any, Dict
from django.views.generic import TemplateView


class ModelFieldsContextMixin:
    model: Model = None

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        model = self.model

        if model:
            fields = [field.verbose_name for field in model._meta.fields]
            objects = model.objects.all()
            context['fields'] = fields
            context['objects'] = objects
            context['model_name'] = model._meta.verbose_name_plural
        return context
