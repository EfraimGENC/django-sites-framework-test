from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site

from django.http import HttpResponse

# Create your views here.
def product_detail(request):
    site = get_current_site(request)
    print(site,"<<<")
    return HttpResponse('Hoppala')