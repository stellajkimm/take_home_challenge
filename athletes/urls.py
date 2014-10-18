from django.conf.urls import patterns, url
from athletes import views

# urlpatterns = patterns('',
#     # ex: /polls/
#     url(r'^$', views.index, name='index'),
#     # ex: /polls/5/
#     url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
#     # ex: /polls/5/results/
#     url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
#     # ex: /polls/5/vote/
#     url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
# )

urlpatterns = patterns('athletes.views',
    url(r'^$', 'index', name='index'),
    # url(r'^sports/$', 'athletes.views.sport_detail', name='detail'),
    # url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    # url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
    url (r'^sports/(?P<sport_id>[0-9]+)/league/(?P<league_id>[0-9]+)/division/(?P<division_id>[0-9]+)/team/(?P<team_id>[0-9]+)/$', views.team_list, name='team_list'),
    url (r'^sports/(?P<sport_id>[0-9]+)/league/(?P<league_id>[0-9]+)/division/(?P<division_id>[0-9]+)/$', views.division_list, name='division_list'),
    url (r'^sports/(?P<sport_id>[0-9]+)/league/(?P<league_id>[0-9]+)/$', views.league_list, name='league_list'),
    url (r'^sports/(?P<sport_id>[0-9]+)/$', views.sport_list, name='sport_list'),

)

# urlpatterns = [
#     url(r'^$', views.index, name='index'),
#     url(r'^players/$', views.players, name='players'),
#     url(r'^players/create/$', views.create, name='create'),
#     url(r'^players/edit/(?P<player_id>\d+)/$', views.edit, name='edit'),
#     url(r'^players/delete/(?P<player_id>\d+)/$', views.delete, name='delete'),
# ]