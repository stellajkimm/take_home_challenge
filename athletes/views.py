from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views import generic

from athletes.models import Sport, League, Division, Team, Athlete

def index(request):
	sports = Sport.objects.all()
	athletes = Athlete.objects.all()
	return render(request, 'athletes/index.html', {'sports': sports, 'athletes': athletes})