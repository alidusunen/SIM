from django.urls import path
from .views import *

app_name = 'custodians'

urlpatterns = [
    path('', view_custodians, name='view_custodians'),
    path('<int:custodian_id>/', custodian_details, name='custodian-detail'),
    path('create/', custodian_create, name='create'),
    path('<int:custodian_id>/update', custodian_update, name='custodian-update'),
    path('<int:custodian_id>/delete', custodian_delete, name='custodian-delete')
]
