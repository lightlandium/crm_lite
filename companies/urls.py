from django.urls import path
from .views import (
    CompanyCreateView, CompanyRetrieveUpdateDestroyView, CompanyRetrieveView,
    StorageCreateView, StorageRetrieveUpdateDestroyView, StorageRetrieveForEmployeesView
)

urlpatterns = [
    path('create/', CompanyCreateView.as_view(), name='company-create'),
    path('<int:pk>/', CompanyRetrieveView.as_view(), name='company-detail'),
    path('<int:pk>/edit/', CompanyRetrieveUpdateDestroyView.as_view(), name='company-edit'),
    path('<int:pk>/storage/create/', StorageCreateView.as_view(), name='storage-create'),
    path('storage/<int:pk>/', StorageRetrieveForEmployeesView.as_view(), name='storage-detail-employee'),
    path('storage/<int:pk>/edit/', StorageRetrieveUpdateDestroyView.as_view(), name='storage-edit'),
]