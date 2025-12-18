from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=200)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    # Additional details
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField()
    date_of_birth = models.DateField(blank=True, null=True)
    date_hired = models.DateField(auto_now_add=True) 
    emergency_contact = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
