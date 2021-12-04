from django.db import models
from django.contrib.sites.models import Site
from django.shortcuts import redirect, reverse

# Create your models here.
class Channel(models.Model):

    name = models.CharField(max_length=150)
    site = models.ForeignKey(Site, related_name='channels', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Channel"
        verbose_name_plural = "Channels"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("channel_detail", kwargs={"pk": self.pk})
