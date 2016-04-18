from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import View


# class Baz(View):
#     PASSWORD = "xyzzy"
#
#
# class Foo(Baz):
#     def get(self, request):
#         assert False, "XYZ"
#
#     def post(self, request):
#         assert False, "ABC"
#
# class Bar(Baz):
#     def get(self, request):
#         assert False, "XYZ"
#
#     def post(self, request):
#         assert False, "ABC"


# def foo(request):
#     assert False, "XXXXX"



urlpatterns = [
    # url(r'foo/', Foo.as_view()),
    url(r'^w/', include('wanted.urls', namespace="wanted")),
    url(r'^admin/', admin.site.urls),
]
