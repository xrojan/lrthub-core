from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Gender(models.Model):
    name = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Nationality(models.Model):
    name = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class EmploymentType(models.Model):
    name = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class MaritalStatus(models.Model):
    name = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Disabilities(models.Model):
    name = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_image = models.CharField(max_length=255)
    mobile_no = models.CharField(max_length=255)

    # demographic categories
    birth_date = models.DateField()
    address = models.TextField()
    children_count = models.IntegerField(default=0)
    salary = models.IntegerField(default=0)
    no_of_cars = models.IntegerField(default=0)

    # demographic categories with references
    gender = models.ForeignKey(Gender, on_delete=models.PROTECT)
    nationality = models.ForeignKey(Nationality, on_delete=models.PROTECT)
    marital_status_id = models.ForeignKey(MaritalStatus, on_delete=models.PROTECT)
    employment_status_id = models.ForeignKey(EmploymentType, on_delete=models.PROTECT)
    disabilities = models.ManyToManyField(Disabilities)

    is_verified = models.BooleanField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % self.user_id.username
