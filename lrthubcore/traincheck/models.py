from django.db import models


# Create your models here.

class TrainCheckHistory(models.Model):
    no_of_faces = models.IntegerField(default=0)
    no_of_male = models.IntegerField(default=0)
    no_of_female = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return "%s" % self.created_on
