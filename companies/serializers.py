from rest_framework import serializers
from .models import Company, Storage

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'inn', 'owner', 'created_at')
        read_only_fields = ('owner', 'created_at')

class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = ('id', 'address', 'company')
        read_only_fields = ('company',)