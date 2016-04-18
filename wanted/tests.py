from django.test import TestCase

from . import models


class WantedTestCase(TestCase):
    def test_ad(self):
        o = models.Ad()
        o.title = "Great Job!"
        o.description = "lore ipsum\n" * 10
        o.apply_email = "udi@company.com"
        o.phone = "09-87654321"

        o.save()
