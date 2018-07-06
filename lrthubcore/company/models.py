from django.db import models


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    vision = models.TextField()
    mission = models.TextField()
    cover_image = models.CharField(max_length=255)
    contact_description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Company Profile Settings'
