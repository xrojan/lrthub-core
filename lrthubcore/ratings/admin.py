from django.contrib import admin
from .models import Rating


# Register your models here.
@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_on'
    search_fields = ['user_id', 'value']
    list_display = ('user_id', 'value',)
    list_filter = ('user_id', 'value', 'is_deleted')
