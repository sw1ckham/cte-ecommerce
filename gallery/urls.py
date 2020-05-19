from django.conf.urls import url, include
from .views import all_canvas, all_paper

urlpatterns = [
    url(r'^paper/', all_paper, name='paper'),
    url(r'^canvas/', all_canvas, name='canvas')
]