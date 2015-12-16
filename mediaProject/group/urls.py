from django.conf.urls import url
from .views import group_list, group_detail, create_group, join_group

urlpatterns = [
    url(r'^list/$', group_list, name='group_list'),
    url(r'^(?P<pk>[0-9]+)/$', group_detail, name='group_detail'),

    url(r'^create/$', create_group, name='create_group'),
    url(r'^join/(?P<id>[0-9]+)/$', join_group, name='join_group'),
]