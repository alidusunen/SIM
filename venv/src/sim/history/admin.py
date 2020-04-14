from django.contrib import admin

# Register your models here.
from .models import Custodian
admin.site.register(Custodian)

from .models import History
admin.site.register(History)

from .models import Asset
admin.site.register(Asset)