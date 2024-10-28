from django.db.models import Model
from typing import Any, Dict
from django.urls import reverse
from django.views.generic import TemplateView


class ModelContextMixin:
    model: Model = None
    paginate_by = 10

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()

        form = self.get_form()
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_queryset(self):
        return self.model.objects.all().select_related()

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        model = self.model

        if model:
            fields = [field.verbose_name for field in model._meta.fields]
            context['fields'] = fields
            context['form'] = self.get_form()
            context['model_name'] = model._meta.verbose_name_plural
        
        return context

    

class ModelSuccessUrlMixin:
    def get_success_url(self):
        model_name = self.model.__name__.lower()
        return reverse(f"{model_name}_list")