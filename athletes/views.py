from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views import generic

from athletes.models import Sport, League, Division, Team, Athlete

def index(request):
	sports = Sport.objects.all()
	athletes = Athlete.objects.all()
	return render(request, 'athletes/index.html', {'sports': sports, 'athletes': athletes})

def sport_list(request, sport_id):
	sport = get_object_or_404(Sport, pk=sport_id)
	sports = Sport.objects.all()
	leagues = sport.league_set.all()
	athletes = Athlete.objects.all().filter(team__division__league__sport=sport)
	return render(request, 'athletes/sport_list.html', {'sport': sport, 'sports': sports, 'athletes': athletes, 'leagues': leagues})

def league_list(request, sport_id, league_id):
	sport = get_object_or_404(Sport, pk=sport_id)
	league = get_object_or_404(League, pk=league_id)
	sports = Sport.objects.all()
	leagues = sport.league_set.all()
	divisions = league.division_set.all()
	athletes = Athlete.objects.all().filter(team__division__league=league)
	return render(request, 'athletes/sport_list.html', {'sport': sport, 'sports': sports, 'athletes': athletes, 'leagues': leagues, 'league': league, 'divisions': divisions})