from django.shortcuts import get_object_or_404, render, redirect
from django.core.urlresolvers import reverse
from django.views import generic
from django import forms

from athletes.models import Sport, League, Division, Team, Athlete

def index(request):
	sports = Sport.objects.order_by('name')
	athletes = Athlete.objects.order_by('last_name')
	teams = Team.objects.order_by('name')
	athlete_form = AthleteForm(request.POST)
	athlete_form.fields['team'] = forms.ModelChoiceField(teams)
	return render(request, 'athletes/index.html', {'sports': sports, 'athletes': athletes, 'teams': teams, 'athlete_form': athlete_form})

def sport_list(request, sport_id):
	sport = get_object_or_404(Sport, pk=sport_id)
	sports = Sport.objects.order_by('name')
	leagues = sport.league_set.order_by('name')
	teams = Team.objects.order_by('name')
	athletes = Athlete.objects.filter(team__division__league__sport=sport).order_by('last_name')
	athlete_form = AthleteForm(request.POST)
	athlete_form.fields['team'] = forms.ModelChoiceField(teams)
	return render(request, 'athletes/index.html', {'sport': sport, 'sports': sports, 'athletes': athletes, 'leagues': leagues, 'teams': teams, 'athlete_form': athlete_form})

def league_list(request, sport_id, league_id):
	sport = get_object_or_404(Sport, pk=sport_id)
	league = get_object_or_404(League, pk=league_id)
	sports = Sport.objects.order_by('name')
	leagues = sport.league_set.order_by('name')
	divisions = league.division_set.order_by('name')
	teams = Team.objects.filter(division__league=league).order_by('name')
	athletes = Athlete.objects.filter(team__division__league=league).order_by('last_name')
	athlete_form = AthleteForm(request.POST)
	athlete_form.fields['team'] = forms.ModelChoiceField(teams)
	return render(request, 'athletes/index.html', {'sport': sport, 'sports': sports, 'athletes': athletes, 'leagues': leagues, 'league': league, 'divisions': divisions, 'teams': teams, 'athlete_form': athlete_form})

def division_list(request, sport_id, league_id, division_id):
	sport = get_object_or_404(Sport, pk=sport_id)
	league = get_object_or_404(League, pk=league_id)
	division = get_object_or_404(Division, pk=division_id)
	sports = Sport.objects.order_by('name')
	leagues = sport.league_set.order_by('name')
	divisions = league.division_set.order_by('name')
	teams = division.team_set.order_by('name')
	athletes = Athlete.objects.filter(team__division=division).order_by('last_name')
	athlete_form = AthleteForm(request.POST)
	athlete_form.fields['team'] = forms.ModelChoiceField(teams)
	return render(request, 'athletes/index.html', {'sport': sport, 'sports': sports, 'athletes': athletes, 'leagues': leagues, 'league': league, 'divisions': divisions, 'division': division, 'teams': teams, 'athlete_form': athlete_form})

def team_list(request, sport_id, league_id, division_id, team_id):
	sport = get_object_or_404(Sport, pk=sport_id)
	league = get_object_or_404(League, pk=league_id)
	division = get_object_or_404(Division, pk=division_id)
	team = get_object_or_404(Team, pk=team_id)
	sports = Sport.objects.order_by('name')
	leagues = sport.league_set.order_by('name')
	divisions = league.division_set.order_by('name')
	teams = division.team_set.order_by('name')
	athletes = Athlete.objects.filter(team=team).order_by('last_name')
	athlete_form = AthleteForm(request.POST)
	athlete_form.fields['team'] = forms.ModelChoiceField(teams)
	return render(request, 'athletes/index.html', {'sport': sport, 'sports': sports, 'athletes': athletes, 'leagues': leagues, 'league': league, 'divisions': divisions, 'division': division, 'teams': teams, 'team': team, 'athlete_form': athlete_form})

def athlete_create(request):
	athlete_form = AthleteForm(request.POST)
	if athlete_form.is_valid():
		athlete_form.save()
		return redirect('index')
	return render(request, 'athletes/index.html')

def athlete_edit(request, athlete_id):
    athlete = get_object_or_404(Athlete, pk=athlete_id)
    edit_athlete_form = AthleteForm(request.POST, instance=athlete)
    if edit_athlete_form.is_valid():
        edit_athlete_form.save()
        return redirect('index')
    return render(request, 'athletes/index.html')

def athlete_delete(request, athlete_id):
	athlete = get_object_or_404(Athlete, pk=athlete_id)
	if request.method=='POST':
		athlete.delete()
		return redirect('index')
	return render(request, 'athletes/index.html')


class AthleteForm(forms.ModelForm):
    class Meta:
        model = Athlete
        fields = ('first_name', 'last_name', 'position', 'number', 'team')








