from django.db import models
from django.conf import settings

class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    inn = models.CharField(max_length=12, unique=True)
    owner = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='owned_company'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Storage(models.Model):
    address = models.CharField(max_length=255)
    company = models.OneToOneField(
        Company,
        on_delete=models.CASCADE,
        related_name='storage'
    )

    def __str__(self):
        return f"Склад {self.company.name} - {self.address}"