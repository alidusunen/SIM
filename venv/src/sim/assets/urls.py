from django.urls import path
from assets.views import list_view, detail_view, create_view, assign_view, update_view, delete_view

app_name = 'assets'
urlpatterns = [
    path('list_view/', list_view, name='list-view'),
    path('<int:asset_id>/', detail_view, name='asset-detail'),
    path('<int:asset_id>/update/', update_view, name='asset-update'),
    path('create/', create_view, name='asset-create'),
    path('<int:asset_id>/delete/', delete_view, name='asset-delete'),
    path('<int:asset_id>/assign/', assign_view, name='asset-assign'),
]