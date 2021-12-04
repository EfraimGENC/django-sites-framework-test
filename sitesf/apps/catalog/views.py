from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from .models import Product
from django.contrib.sites.models import Site
from sitesf.apps.channel.models import Channel


# Create your views here.
def product_list(request):
    products = Product.objects.filter(channels__site=request.site).distinct()
    return render(request, 'product_detail.html', {'products': products})