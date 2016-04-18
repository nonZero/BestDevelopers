"""bestdevelopers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.http.response import HttpResponse


def foo(request):
    # assert False, "asdljhsak"
    return HttpResponse("Hello world!")


def hello(request, name, age):
    message = "Hello {} you are {} years old!".format(name, age)
    return HttpResponse(message)


def add(request, a, b):
    message = "{} + {} = {}".format(a, b, int(a) + int(b))
    return HttpResponse(message)


# /add/10/20/
# 10 + 20 = 30

urlpatterns = [
    url(r'^$', foo),
    url(r'^hello/(?P<name>\w+)/(?P<age>\d+)/$', hello),
    url(r'^hello/(?P<age>\d+)/(?P<name>\w+)/$', hello),
    url(r'^hello/(?P<name>\w+)/$', hello, kwargs={'age': 13}),
    url(r'^hello/$', hello, kwargs={'name':'kuku,', 'age': 13}),
    url(r'^add/(\d+)/(\d+)/$', add),
    url(r'^admin/', admin.site.urls),
]
