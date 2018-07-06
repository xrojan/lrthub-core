from django.contrib import admin

# Register your models here.
from .models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_on'
    list_display = ('name', 'description', 'vision', 'mission')

    def has_add_permission(self, request):
        """
        Prevents duplicate instance of company profile's record
        :param request:
        :return:
        """
        base_add_permission = super(CompanyAdmin, self).has_add_permission(request)
        if base_add_permission:
            count = Company.objects.all().count()
            if count == 0:
                return True
        return False

    def has_delete_permission(self, request, obj=None):
        """
        Prevents deletion of company profile record as this model serves
        as a single record storage for company's whereabouts
        :param request:
        :param obj:
        :return:
        """
        return False


admin.site.index_title = "LRTHub"
admin.site.site_title = "Core Administration"
admin.site.site_header = "LRTHub Core"
