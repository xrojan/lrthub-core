from django.contrib import admin
from .models import FeedbackConversation, FeedbackMessage

# Register your models here.
admin.site.register(FeedbackConversation)
admin.site.register(FeedbackMessage)
