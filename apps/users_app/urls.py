from django.conf.urls import url
from . import views 
urlpatterns = [
url(r'^$', views.index),
url(r'^login$', views.login),
url(r'^new$', views.index),
url(r'^users$', views.allUsers),
]