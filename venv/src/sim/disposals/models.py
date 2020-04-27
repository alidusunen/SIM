from django.db import models
from django.urls import reverse
from datetime import date

from assets.models import Asset

class Disposal(models.Model):

    documentNumber = models.CharField(max_length=40)
    date = models.DateField(auto_now=False, auto_now_add=False)
    base = models.CharField(max_length=40, default="")
    reason = models.CharField(max_length=80, default="")
    comments = models.CharField(max_length=140, default="")
    assets = models.ManyToManyField(Asset)

    def get_absolute_url(self):
        return reverse("disposals:disposal-detail", kwargs={"id":self.id})

# Create your models here.
