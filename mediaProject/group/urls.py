from django.conf.urls import url
from .views import group_list


urlpatterns = [
    url(r'^list/$', group_list, name='group_list'),
]