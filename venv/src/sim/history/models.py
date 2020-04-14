from django.db import models
from custodians.models import Custodian
from assets.models import Asset

class History(models.Model):
    asset_id = models.ForeignKey(Asset, on_delete=models.CASCADE)
    custodian_id = models.ForeignKey(Custodian, on_delete=models.CASCADE)
    history_date = models.DateField(auto_now_add=True)

    def get_asset_url(self):
        return reverse("reports:report-asset", kwargs={"asset_id":self.asset_id})

    def get_custodian_url(self):
        return reverse("reports:report-custodian", kwargs={"custodian_id":self.custodian_id})
