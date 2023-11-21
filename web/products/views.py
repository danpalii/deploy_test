from django.shortcuts import render
from django.views.generic import TemplateView
from .services.products import get_all_products
class Home(TemplateView):
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = get_all_products()
        return context
