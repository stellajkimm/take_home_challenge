from django.shortcuts import get_object_or_404, render, redirect
from django.core.urlresolvers import reverse
from django.views import generic
from django import forms
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from urlparse import urlparse

from athletes.models import Sport, League, Division, Team, Athlete

def index(request):
	"""
	main view that lists all athletes
	"""
	sports = Sport.objects.order_by('name')
	teams = Team.objects.order_by('name')
	athlete_form = AthleteForm(request.POST)
	athlete_form.fields['team'] = forms.ModelChoiceField(teams)
	athletes = Athlete.objects.order_by('last_name')
	data = {'sports': sports, 'athletes': athletes, 'teams': teams, 'athlete_form': athlete_form}
	return render(request, 'athletes/index.html', data)

def sport_list(request, sport_id):
	"""
	lists all athletes within a specific sport using sport_id
	"""
	sport = get_object_or_404(Sport, pk=sport_id)
	sports = Sport.objects.order_by('name')
	leagues = sport.league_set.order_by('name')
	teams = Team.objects.filter(division__league__sport=sport).order_by('name')
	athletes = Athlete.objects.filter(team__division__league__sport=sport).order_by('last_name')
	athlete_form = AthleteForm(request.POST)
	athlete_form.fields['team'] = forms.ModelChoiceField(teams)
	data = {'sport': sport, 'sports': sports, 'athletes': athletes, 'leagues': leagues, 'teams': teams, 'athlete_form': athlete_form}
	return render(request, 'athletes/index.html', data)

def league_list(request, league_id):
	"""
	lists all athletes within a specific league using league_id
	"""
	league = get_object_or_404(League, pk=league_id)
	sports = Sport.objects.order_by('name')
	leagues = league.sport.league_set.order_by('name')
	divisions = league.division_set.order_by('name')
	teams = Team.objects.filter(division__league=league).order_by('name')
	athletes = Athlete.objects.filter(team__division__league=league).order_by('last_name')
	athlete_form = AthleteForm(request.POST)
	athlete_form.fields['team'] = forms.ModelChoiceField(teams)
	data = {'sport': league.sport, 'sports': sports, 'athletes': athletes, 'leagues': leagues, 'league': league, 'divisions': divisions, 'teams': teams, 'athlete_form': athlete_form}
	return render(request, 'athletes/index.html', data)

def division_list(request, division_id):
	"""
	lists all athletes within a specific division using division_id
	"""
	division = get_object_or_404(Division, pk=division_id)
	sports = Sport.objects.order_by('name')
	leagues = division.league.sport.league_set.order_by('name')
	divisions = division.league.division_set.order_by('name')
	teams = division.team_set.order_by('name')
	athletes = Athlete.objects.filter(team__division=division).order_by('last_name')
	athlete_form = AthleteForm(request.POST)
	athlete_form.fields['team'] = forms.ModelChoiceField(teams)
	data = {'sport': division.league.sport, 'sports': sports, 'athletes': athletes, 'leagues': leagues, 'league': division.league, 'divisions': divisions, 'division': division, 'teams': teams, 'athlete_form': athlete_form}
	return render(request, 'athletes/index.html', data)

def team_list(request, team_id):
	"""
	lists all athletes within a specific team using team_id
	"""
	team = get_object_or_404(Team, pk=team_id)
	sports = Sport.objects.order_by('name')
	leagues = team.division.league.sport.league_set.order_by('name')
	divisions = team.division.league.division_set.order_by('name')
	teams = team.division.team_set.order_by('name')
	athletes = Athlete.objects.filter(team=team).order_by('last_name')
	athlete_form = AthleteForm(request.POST)
	athlete_form.fields['team'] = forms.ModelChoiceField(Team.objects.filter(id=team_id))
	data = {'sport': team.division.league.sport, 'sports': sports, 'athletes': athletes, 'leagues': leagues, 'league': team.division.league, 'divisions': divisions, 'division': team.division, 'teams': teams, 'team': team, 'athlete_form': athlete_form}
	return render(request, 'athletes/index.html', data)

def athlete_create(request):
	athlete_form = AthleteForm(request.POST)
	referer = urlparse(request.META.get('HTTP_REFERER')).path
	print referer
	if athlete_form.is_valid():
		athlete_form.save()
		return redirect(referer)
	return render(request, 'athletes/index.html')

def athlete_edit(request, athlete_id):
    athlete = get_object_or_404(Athlete, pk=athlete_id)
    referer = urlparse(request.META.get('HTTP_REFERER')).path
    edit_athlete_form = AthleteForm(request.POST, instance=athlete)
    if edit_athlete_form.is_valid():
        edit_athlete_form.save()
        return redirect(referer)
    return render(request, 'athletes/index.html')

def athlete_delete(request, athlete_id):
	athlete = get_object_or_404(Athlete, pk=athlete_id)
	referer = urlparse(request.META.get('HTTP_REFERER')).path
	if request.method=='POST':
		athlete.delete()
		return redirect(referer)
	return render(request, 'athletes/index.html')

def sport_create(request):
	sport_form = SportForm(request.POST)
	if sport_form.is_valid():
		sport = sport_form.save()
		return redirect('sport_list', sport.id)
	return render(request, 'athletes/index.html')

def league_create(request):
	league_form = LeagueForm(request.POST)
	if league_form.is_valid():
		league = league_form.save()
		return redirect('league_list', league.id)
	return render(request, 'athletes/index.html')

def division_create(request):
	division_form = DivisionForm(request.POST)
	if division_form.is_valid():
		division = division_form.save()
		return redirect('division_list', division.id)
	return render(request, 'athletes/index.html')

def team_create(request):
	team_form = TeamForm(request.POST)
	if team_form.is_valid():
		team = team_form.save()
		return redirect('team_list', team.id)
	return render(request, 'athletes/index.html')


class AthleteForm(forms.ModelForm):
    class Meta:
        model = Athlete
        fields = ('first_name', 'last_name', 'position', 'number', 'team')

class SportForm(forms.ModelForm):
    class Meta:
        model = Sport
        fields = ('name',)

class LeagueForm(forms.ModelForm):
    class Meta:
        model = League
        fields = ('name', 'sport')

class DivisionForm(forms.ModelForm):
    class Meta:
        model = Division
        fields = ('name', 'league')

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ('name', 'division')





