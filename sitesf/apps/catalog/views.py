from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from .models import Product
from django.contrib.sites.models import Site
from sitesf.apps.channel.models import Channel
from django.views.generic import ListView
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.views.decorators.vary import vary_on_cookie


# Create your views here.
@method_decorator([vary_on_cookie, cache_page(60)], name='dispatch')
class ProductList(ListView):
    model = Product
    template_name='product_detail.html'

    def get_queryset(self):
        return self.model.objects.filter(channels__site=self.request.site).distinct()
