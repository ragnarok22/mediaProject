from django.conf.urls import include, url
from django.contrib import admin
from .settings import MEDIA_ROOT


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^pictures/', include('picture.urls', namespace='picture')),
    url(r'^group/', include('group.urls', namespace='group')),
    url(r'^', include('account.urls', namespace='account')),

    url(r'^(?P<path>.*)/$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
]
