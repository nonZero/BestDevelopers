from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.AdListView.as_view(), name="list"),
    url(r'^api/$', views.AdJsonView.as_view(), name="api"),
    url(r'^(?P<pk>\d+)/$', views.AdDetailView.as_view(), name="detail"),
    url(r'^(?P<pk>\d+)/edit/$', views.AdUpdateView.as_view(), name="update"),
    url(r'^(?P<pk>\d+)/delete/$', views.AdDeleteView.as_view(), name="delete"),
    url(r'^add/$', views.AdCreateView.as_view(), name="add"),
    url(r'^contact/$', views.ContactUsView.as_view(), name="contact"),
]
