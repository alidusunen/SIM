from django.urls import path
from allocations.views import create_view

app_name = 'allocations'
urlpatterns = [
    # path('list_view/', list_view, name='list-view'),
    # path('<int:asset_id>/', detail_view, name='asset-detail'),
    path('create/', create_view, name='allocations-create'),
    # path('<int:asset_id>/assign/', assign_view, name='asset-assign'),
]