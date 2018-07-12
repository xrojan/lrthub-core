from django.contrib import admin

# Register your models here.
from .models import Faq


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    date_hierarchy = 'updated_at'
    list_display = ('question', 'answer', 'created_on', 'updated_at')
    search_fields = ('question', 'answer',)
