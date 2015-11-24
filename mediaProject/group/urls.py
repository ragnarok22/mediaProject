from django.conf.urls import url
from .views import group_list, group_detail


urlpatterns = [
    url(r'^list/$', group_list, name='group_list'),
    url(r'^(?P<pk>[0-9]+)/$', group_detail, name='group_detail'),
]