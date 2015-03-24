from django.conf.urls import patterns, url

from app import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^team/$', views.team, name='team'),
    url(r'^player/$', views.player, name='player'),
)