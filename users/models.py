from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_company_owner = models.BooleanField(default=False)
    company = models.ForeignKey(
        'companies.Company',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='employees'
    )

    def __str__(self):
        return self.email
