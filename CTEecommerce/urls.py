"""CTEecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as urls_accounts
from home import urls as urls_home
from product import urls as urls_product
from cart import urls as urls_cart
from checkout import urls as urls_checkout
from gallery import urls as urls_gallery
from accounts.views import index
from home.views import about
from product.views import all_products
from django.views import static
from .settings import MEDIA_ROOT


urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^home/', include(urls_home)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^product/', all_products, name="product"),
    url(r'^cart/', include(urls_cart)),
    url(r'^gallery/', include(urls_gallery)),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT})
]
