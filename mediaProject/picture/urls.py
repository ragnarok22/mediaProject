from django.conf.urls import url
from .views import pictures_list, picture_details


urlpatterns = [
    url(r'^list/$', pictures_list, name='pictures_list'),
    url(r'^(?P<pk>[0-9]+)/$', picture_details, name='pictures_details'),

]
