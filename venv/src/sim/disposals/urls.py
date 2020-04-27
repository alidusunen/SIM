from django.urls import path
from disposals.views import create_view, detail_view, list_view, delete_view

app_name = 'disposals'
urlpatterns = [
    path('', list_view, name='list-view'),
    path('<int:id>/', detail_view, name='disposal-detail'),
    path('create/', create_view, name='create'),
    path('<int:id>/delete', delete_view, name='disposal-delete'),
]