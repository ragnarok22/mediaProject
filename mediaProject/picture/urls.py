from django.conf.urls import url
from .views import pictures_list


urlpatterns = [
    url(r'^list/$', pictures_list, name='pictures_list'),

]
