from django.db import models
from custodians.models import Custodian
from django.urls import reverse

class Asset(models.Model):
    tag_number = models.CharField(max_length=18)
    description = models.CharField(max_length=80)
    price = models.DecimalField(decimal_places=2, max_digits=8, default=123)
    custodian = models.ForeignKey(Custodian, blank=True, null=True, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("assets:asset-detail", kwargs={"asset_id":self.id})

# Create your models here.
