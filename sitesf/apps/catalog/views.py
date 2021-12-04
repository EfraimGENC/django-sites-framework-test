from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from .models import Product
from django.contrib.sites.models import Site
from sitesf.apps.channel.models import Channel
from django.views.generic import ListView

# Create your views here.
class ProductList(ListView):
    model = Product
    template_name='product_detail.html'

    def get_queryset(self):
        return self.model.objects.filter(channels__site=self.request.site).distinct()
