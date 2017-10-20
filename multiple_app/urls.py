
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^blogs/', include('apps.next_app.urls')),

    url(r'^surveys/', include('apps.surveys_app.urls')),
    
    url(r'^register/', include('apps.users_app.urls')),
    url(r'^login/', include('apps.users_app.urls')),
    url(r'^users/', include('apps.users_app.urls')),

]
