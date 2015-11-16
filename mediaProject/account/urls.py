from django.conf.urls import url
from .views import login_view, terms, about, privacy, dashboard, logout_view, contact_us, user_login, friendship
from mediaProject.settings import MEDIA_ROOT


urlpatterns = [
    url(r'^login/$', login_view, name='login'),
    url(r'^logout/$', logout_view, name='logout'),

    url(r'^dashboard/$', dashboard, name='dashboard'),

    url(r'^users/in/$', user_login, name='user_login'),
    url(r'^friendship/$', friendship, name='friendship'),

    url(r'^contact/us/$', contact_us, name='contact'),
    url(r'^terms/$', terms, name='terms'),
    url(r'^about/$', about, name='about'),
    url(r'^privacy/$', privacy, name='privacy'),

    url(r'^(?P<path>.*)/$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),


]