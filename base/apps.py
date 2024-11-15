from django.apps import AppConfig
from watson import search


class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'

    def ready(self):
        import base.singnals
        all_models = self.get_models()
        
        for model in all_models:
            search.register(model)