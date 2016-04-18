from django.db import models


class Ad(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=500)
    description = models.TextField()
    contact_person = models.CharField(max_length=100)
    apply_email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
