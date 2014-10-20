from django.shortcuts import get_object_or_404, render, redirect
from django.core.urlresolvers import reverse
from django.views import generic
from django import forms

from athletes.models import Sport, League, Division, Team, Athlete

def index(request):
	sports = Sport.objects.order_by('name')
	athletes = Athlete.objects.order_by('last_name')
	create_athlete_form = AthleteForm(request.POST)
	create_athlete_form.fields['team'] = forms.ModelChoiceField(Team.objects.order_by('name'))
	return render(request, 'athletes/index.html', {'sports': sports, 'athletes': athletes, 'create_athlete_form': create_athlete_form})

def sport_list(request, sport_id):
	sport = get_object_or_404(Sport, pk=sport_id)
	sports = Sport.objects.order_by('name')
	leagues = sport.league_set.order_by('name')
	teams = Team.objects.order_by('name')
	athletes = Athlete.objects.filter(team__division__league__sport=sport).order_by('last_name')
	create_athlete_form = AthleteForm(request.POST)
	create_athlete_form.fields['team'] = forms.ModelChoiceField(teams)
	return render(request, 'athletes/index.html', {'sport': sport, 'sports': sports, 'athletes': athletes, 'leagues': leagues, 'create_athlete_form': create_athlete_form})

def league_list(request, sport_id, league_id):
	sport = get_object_or_404(Sport, pk=sport_id)
	league = get_object_or_404(League, pk=league_id)
	sports = Sport.objects.order_by('name')
	leagues = sport.league_set.order_by('name')
	divisions = league.division_set.order_by('name')
	teams = Team.objects.filter(division__league=league).order_by('name')
	athletes = Athlete.objects.filter(team__division__league=league).order_by('last_name')
	create_athlete_form = AthleteForm(request.POST)
	create_athlete_form.fields['team'] = forms.ModelChoiceField(teams)
	return render(request, 'athletes/index.html', {'sport': sport, 'sports': sports, 'athletes': athletes, 'leagues': leagues, 'league': league, 'divisions': divisions, 'create_athlete_form': create_athlete_form})

def division_list(request, sport_id, league_id, division_id):
	sport = get_object_or_404(Sport, pk=sport_id)
	league = get_object_or_404(League, pk=league_id)
	division = get_object_or_404(Division, pk=division_id)
	sports = Sport.objects.order_by('name')
	leagues = sport.league_set.order_by('name')
	divisions = league.division_set.order_by('name')
	teams = division.team_set.order_by('name')
	athletes = Athlete.objects.filter(team__division=division).order_by('last_name')
	create_athlete_form = AthleteForm(request.POST)
	create_athlete_form.fields['team'] = forms.ModelChoiceField(teams)
	return render(request, 'athletes/index.html', {'sport': sport, 'sports': sports, 'athletes': athletes, 'leagues': leagues, 'league': league, 'divisions': divisions, 'division': division, 'teams': teams, 'create_athlete_form': create_athlete_form})

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
	create_athlete_form = AthleteForm(request.POST)
	create_athlete_form.fields['team'] = forms.ModelChoiceField(teams)
	return render(request, 'athletes/index.html', {'sport': sport, 'sports': sports, 'athletes': athletes, 'leagues': leagues, 'league': league, 'divisions': divisions, 'division': division, 'teams': teams, 'team': team, 'create_athlete_form': create_athlete_form})

def athlete_delete(request, athlete_id):
	# template_name='athletes/athlete_confirm_delete.html'
	athlete = get_object_or_404(Athlete, pk=athlete_id)
	if request.method=='POST':
			athlete.delete()
			return redirect('index')
	return render(request, 'athletes/index.html', {'athlete':athlete})

# def get_name(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         create_athlete_form = AthleteForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('/thanks/')

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = NameForm()

#     return render(request, 'name.html', {'form': form})

class AthleteForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    position = forms.CharField(label='Position', max_length=100)
    number = forms.CharField(label='Number', max_length=100)

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Athlete
        fields = ('first_name', 'last_name', 'position', 'number', 'team')








