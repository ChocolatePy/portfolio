from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^gallery/$', views.gallery, name='gallery'),
]

