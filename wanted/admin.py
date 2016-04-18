from django.contrib import admin

from . import models


class AdAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'created_at',
        'apply_email',
        'contact_person',
    )
    search_fields = (
        'title',
        'description',
    )
    # list_filter = (
    #     'verified',
    # )
    date_hierarchy = 'created_at'



admin.site.register(models.Ad, AdAdmin)
