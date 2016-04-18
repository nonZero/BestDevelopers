from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^w/', include('wanted.urls', namespace="wanted")),
    url(r'^admin/', admin.site.urls),
]
