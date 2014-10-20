from django.conf.urls import patterns, url
from athletes import views

urlpatterns = patterns('athletes.views',
    url(r'^$', 'index', name='index'),
    # url(r'^sports/$', 'athletes.views.sport_detail', name='detail'),
    # url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    # url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
    url (r'^sports/(?P<sport_id>[0-9]+)/league/(?P<league_id>[0-9]+)/division/(?P<division_id>[0-9]+)/team/(?P<team_id>[0-9]+)/$', views.team_list, name='team_list'),
    url (r'^sports/(?P<sport_id>[0-9]+)/league/(?P<league_id>[0-9]+)/division/(?P<division_id>[0-9]+)/$', views.division_list, name='division_list'),
    url (r'^sports/(?P<sport_id>[0-9]+)/league/(?P<league_id>[0-9]+)/$', views.league_list, name='league_list'),
    url (r'^sports/(?P<sport_id>[0-9]+)/$', views.sport_list, name='sport_list'),

    url (r'^athletes/delete/(?P<athlete_id>\d+)/$', views.athlete_delete, name='athlete_delete'),
    url (r'^athletes/create/$', views.athlete_create, name='athlete_create'),
    url (r'^athletes/edit/(?P<athlete_id>\d+)/$', views.athlete_edit, name='athlete_edit'),


)

# urlpatterns = [
#     url(r'^$', views.index, name='index'),
#     url(r'^players/$', views.players, name='players'),
#     url(r'^players/create/$', views.create, name='create'),
#     url(r'^players/edit/(?P<player_id>\d+)/$', views.edit, name='edit'),
#     url(r'^players/delete/(?P<player_id>\d+)/$', views.delete, name='delete'),
# ]