from django.conf.urls import patterns, url
from athletes import views

urlpatterns = patterns('athletes.views',
	
    url(r'^$', 'index', name='index'),

    url (r'^sports/(?P<sport_id>[0-9]+)/$', views.sport_list, name='sport_list'),
    url (r'^sports/create/$', views.sport_create, name='sport_create'),
    
    url (r'^league/(?P<league_id>[0-9]+)/$', views.league_list, name='league_list'),
    url (r'^leagues/create/$', views.league_create, name='league_create'),
    
    url (r'^division/(?P<division_id>[0-9]+)/$', views.division_list, name='division_list'),
    url (r'^divisions/create/$', views.division_create, name='division_create'),
    
    url (r'^team/(?P<team_id>[0-9]+)/$', views.team_list, name='team_list'),
    url (r'^teams/create/$', views.team_create, name='team_create'),

    url (r'^athletes/create/$', views.athlete_create, name='athlete_create'),
    url (r'^athletes/edit/(?P<athlete_id>\d+)/$', views.athlete_edit, name='athlete_edit'),
    url (r'^athletes/delete/(?P<athlete_id>\d+)/$', views.athlete_delete, name='athlete_delete'),

    
)
