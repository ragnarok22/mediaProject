from django.conf.urls import url
from .views import pictures_list, picture_details, last_picture


urlpatterns = [
    url(r'^list/$', pictures_list, name='pictures_list'),
    url(r'^(?P<pk>[0-9]+)/$', picture_details, name='pictures_details'),

    url(r'^last/$', last_picture, name='last_picture'),
]
