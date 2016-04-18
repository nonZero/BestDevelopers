from django.test import TestCase

class MyViewsTestCase(TestCase):
    def test_homepage(self):
        resp = self.client.get("/")
        self.assertContains(resp, "Hello")

    def test_multiply(self):
        resp = self.client.get("/mul/5/10/")
        self.assertContains(resp, "50")
