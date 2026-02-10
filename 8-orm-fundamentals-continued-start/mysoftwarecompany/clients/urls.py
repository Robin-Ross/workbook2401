from django.urls import path
from .views import companies_list

urlpatterns = [
  path('companies/', companies_list, name='companies_list')
]