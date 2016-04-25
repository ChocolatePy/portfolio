from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^gallery/$', views.gallery, name='gallery'),
    url(r'^gallery-item-(?P<item_id>\d+)/$', views.gallery_item, name='gallery_item'),

    url(r'^gallery-item-comment/$', views.gallery_item_comment, name='gallery_item_comment'),
] 
