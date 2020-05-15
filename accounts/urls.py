from django.conf.urls import url, include
from accounts.views import logout, login, registration, index
from accounts import url_reset

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^register/', registration, name="register"),
    url(r'^password-reset/', include(url_reset))
]