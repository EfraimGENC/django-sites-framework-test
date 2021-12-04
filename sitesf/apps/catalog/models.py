from django.db import models
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager
from django.shortcuts import redirect, reverse
from sitesf.apps.channel.models import Channel

# Create your models here.
class Product(models.Model):

    name = models.CharField(max_length=150)
    description = models.TextField("Description")
    channels = models.ManyToManyField(Channel)

    objects = models.Manager()

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.pk})
