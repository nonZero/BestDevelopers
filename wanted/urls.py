from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.ad_list, name="list"),
    url(r'^(\d+)/$', views.ad_detail, name="detail"),
    url(r'^add/$', views.ad_add, name="add"),
    url(r'^contact/$', views.contact_us, name="contact"),
]
