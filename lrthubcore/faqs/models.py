from django.db import models


# Create your models here.

class Faq(models.Model):
    question = models.TextField()
    answer = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.question
