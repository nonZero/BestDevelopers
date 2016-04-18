from django.core.urlresolvers import reverse
from django.db import models
from django.utils.six import python_2_unicode_compatible


class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    priority = models.IntegerField(default=10)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.title


class Ad(models.Model):
    category = models.ForeignKey(Category)
    created_at = models.DateTimeField(auto_now_add=True,
                                      db_index=True)
    title = models.CharField(max_length=500)
    description = models.TextField()
    contact_person = models.CharField(max_length=100)
    apply_email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)

    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("wanted:detail", args=(self.id,))
