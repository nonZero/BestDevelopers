from django.contrib import admin

from . import models


class AdAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'created_at',
        'apply_email',
        'contact_person',
    )
    search_fields = (
        'title',
        'description',
    )
    list_filter = (
        'category',
    )
    date_hierarchy = 'created_at'


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'ad_count',
    )

    def ad_count(self, instance):
        return instance.ad_set.count()


admin.site.register(models.Ad, AdAdmin)
admin.site.register(models.Category, CategoryAdmin)
