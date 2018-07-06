from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class FeedbackConversation(models.Model):
    # Customer Complaint Form
    full_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=50)
    employee_name = models.CharField(max_length=255)
    incident_date = models.DateTimeField()
    incident_subject = models.TextField()
    other_details = models.TextField(default=None)
    is_closed = models.BooleanField(default=False)

    # Each complaint form correspond to a unique conversation instance
    sender_id = models.ForeignKey(User, on_delete=models.PROTECT, related_name='sender_user_set')
    receiver_id = models.ForeignKey(User, on_delete=models.PROTECT, related_name='receiver_user_set')

    updated_at = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.incident_subject


class FeedbackMessage(models.Model):
    conversation_id = models.ForeignKey(FeedbackConversation, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return self.message
