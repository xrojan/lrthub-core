from django.contrib import admin
from .models import FeedbackConversation, FeedbackMessage


# Register your models here.
class FeedbackMessagesInline(admin.TabularInline):
    model = FeedbackMessage
    fields = ('message', 'sender_id', 'created_on',)
    readonly_fields = ('created_on', 'message', 'sender_id',)

    def has_add_permission(self, request):
        return False


@admin.register(FeedbackConversation)
class FeedbackConversation(admin.ModelAdmin):
    model = FeedbackConversation
    list_display = ('incident_subject', 'incident_date', 'employee_name', 'full_name', 'contact_number')
    inlines = (FeedbackMessagesInline,)
    readonly_fields = ('sender_id', 'receiver_id')


admin.site.register(FeedbackMessage)
