from django.conf.urls import url, include
from .views import all_products

urlpatters = [
    url(r'^$', all_products, name="product")
]
