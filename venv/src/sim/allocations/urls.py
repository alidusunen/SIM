from django.urls import path
from allocations.views import create_view, detail_view, list_view, delete_view

app_name = 'allocations'
urlpatterns = [
    path('', list_view, name='list-view'),
    path('<int:id>/', detail_view, name='allocation-detail'),
    path('create/', create_view, name='create'),
    path('<int:id>/delete', delete_view, name='allocation-delete'),
]