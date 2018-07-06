from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class FeedbackConversation(models.Model):
    sender_id = models.ForeignKey(User, on_delete=models.PROTECT, related_name='sender_user_set')
    receiver_id = models.ForeignKey(User, on_delete=models.PROTECT, related_name='receiver_user_set')
    updated_at = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.sender_id


class FeedbackMessage(models.Model):
    conversation_id = models.ForeignKey(FeedbackConversation, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return self.message
