from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=20, unique=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    mobile_phone = models.CharField(max_length=15, unique=True, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    id_city = models.ForeignKey('City', on_delete=models.SET_NULL, null=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.first_name
    
class Country(models.Model):
    name = models.CharField(max_length=100)
    abrev = models.CharField(max_length=10, null=True, blank=True)
    status = models.BooleanField(default=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.abrev} {'Active' if self.status else 'Inactive'}" 

    
class Department(models.Model):
    name = models.CharField(max_length= 20, unique=True)
    abrev = models.CharField(max_length=5, null=True, blank=True)
    id_country = models.ForeignKey('Country', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100)
    abrev = models.CharField(max_length=10, null=True, blank=True)
    id_department = models.ForeignKey('Department', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
