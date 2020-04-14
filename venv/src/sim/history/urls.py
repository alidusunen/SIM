from django.urls import path
from history.views import *

app_name = 'reports'
urlpatterns = [
    path('', reports_main, name='reports-main'),
    path('asset/', generate_asset, name='generate-asset'),
    path('custodian/', generate_custodian, name='generate-asset'),
    path('custodian/<int:custodian_id>/', report_custodian, name='report-custodian'),
    path('asset/<int:asset_id>/', report_asset, name='report-asset'),
]