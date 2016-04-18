from django.core.urlresolvers import reverse
from django.db import models
from django.utils.six import python_2_unicode_compatible


@python_2_unicode_compatible
class Ad(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=500)
    description = models.TextField()
    contact_person = models.CharField(max_length=100)
    apply_email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("wanted:detail", args=(self.id,))