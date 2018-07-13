from django.shortcuts import render

# Create your views here.
from django.views import generic

from .models import Faq


class IndexView(generic.ListView):
    template_name = 'faqs/index.html'
    context_object_name = 'latest_faq_list'

    def get_queryset(self):
        return Faq.objects.order_by('-updated_at')
