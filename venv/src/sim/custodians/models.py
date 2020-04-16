from django.db import models
from django.urls import reverse


class Custodian(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    base = models.CharField(max_length=10, default="ERB")

    #To retun name instead od ID number when refered in other areas
    # def __str__(self):
    #     return self.name

    def get_absolute_url(self):
        return reverse("custodians:custodian-detail", kwargs={"custodian_id":self.id})

# Create your models here.
