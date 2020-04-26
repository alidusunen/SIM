from django.db import models
from django.urls import reverse
from datetime import date
from decimal import Decimal

from custodians.models import Custodian
from categories.models import SubCategory

class Asset(models.Model):
    #Asset Details
    tag_number = models.CharField(max_length=18)
    brand = models.CharField(max_length=50, default="")
    model = models.CharField(max_length=100, default="")
    serial = models.CharField(max_length=40, default="")
    sub_category = models.ForeignKey(SubCategory, blank=True, null=True, on_delete=models.SET_NULL)
    description = models.CharField(max_length=120)

    #User and Location Details
    location = models.CharField(max_length=20, default="")
    physical_location = models.CharField (max_length=80, default="")
    condition = models.CharField(max_length=40, default="")
    custodian = models.ForeignKey(Custodian, blank=True, null=True, on_delete=models.CASCADE)
    accessories = models.CharField(max_length=140, default="")

    #Purchase Details
    price = models.DecimalField(decimal_places=2, max_digits=8, default=123)
    donor = models.CharField(max_length=25, default="")
    budgetCode = models.CharField(max_length=25, default="")
    purchaseReference = models.CharField(max_length=45, default="")
    purchaseDate = models.DateField(auto_now=False, auto_now_add=False, default=date.today)
    supplierName = models.CharField(max_length=80, default="2")

    #Other

    comments = models.CharField(max_length=140, default="")


    def get_absolute_url(self):
        return reverse("assets:asset-detail", kwargs={"asset_id":self.id})

    def depreciation(self):
        d1 = self.purchaseDate
        d2 = date.today()
        # Calculate the number of months
        months = (d2.year - d1.year)*12 +(d2.month-d1.month)
        #Calculate the amount of total depreciation
        reduction = self.price*Decimal(months/self.sub_category.depreciation_length)

        result = round(self.price - reduction, 2)

        if result > 0:
            return result

        return 0




# Create your models here.
