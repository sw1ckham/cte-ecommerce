from django.conf.urls import url
from django.contrib import admin
from home.views import about

urlpatterns = [
    url(r'^about/', about, name='about'),
]