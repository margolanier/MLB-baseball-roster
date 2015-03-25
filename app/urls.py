from django.conf.urls import patterns, url

from app import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^team/(?P<team_pk>\d+)$', views.team, name='team'),
    url(r'^player/(?P<player_pk>\d+)$', views.player, name='player'),
)