from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from .models import Company, Storage
from .serializers import CompanySerializer, StorageSerializer
from .permissions import IsCompanyOwner, IsCompanyEmployee

class CompanyCreateView(generics.CreateAPIView):
    serializer_class = CompanySerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        user = self.request.user
        if user.company or hasattr(user, 'owned_company'):
            raise ValidationError("Пользователь уже владеет компанией или привязан к компании.")
        company = serializer.save(owner=user)
        user.is_company_owner = True
        user.company = company
        user.save()

class CompanyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (permissions.IsAuthenticated, IsCompanyOwner)

class CompanyRetrieveView(generics.RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (permissions.IsAuthenticated, IsCompanyEmployee)

class StorageCreateView(generics.CreateAPIView):
    serializer_class = StorageSerializer
    permission_classes = (permissions.IsAuthenticated, IsCompanyOwner)

    def perform_create(self, serializer):
        company = self.request.user.owned_company
        if hasattr(company, 'storage'):
            raise ValidationError("У компании уже есть склад")
        serializer.save(company=company)

class StorageRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer
    permission_classes = (permissions.IsAuthenticated, IsCompanyOwner)

class StorageRetrieveForEmployeesView(generics.RetrieveAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer
    permission_classes = (permissions.IsAuthenticated, IsCompanyEmployee)
