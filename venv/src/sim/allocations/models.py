from django.db import models
from django.urls import reverse
from datetime import date

from assets.models import Asset


class Allocation(models.Model):

    documentNumber = models.CharField(max_length = 40)
    date = models.DateField(auto_now=False, auto_now_add=False)
    previousDonor = models.CharField(max_length=25)
    previousBudget = models.CharField(max_length=25)
    newDonor = models.CharField(max_length=25)
    newBudget = models.CharField(max_length=25)
    comments = models.CharField(max_length = 140)
    assets = models.ManyToManyField(Asset)

    def get_absolute_url(self):
        return reverse("allocations:allocation-detail", kwargs={"id":self.id})
# Create your models here.
