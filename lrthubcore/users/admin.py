from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.UserProfile)
admin.site.register(models.EmploymentType)
admin.site.register(models.Gender)
admin.site.register(models.Nationality)
admin.site.register(models.MaritalStatus)
admin.site.register(models.Disabilities)
