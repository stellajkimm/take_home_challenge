from django.shortcuts import get_object_or_404, render_to_response
from django.core.urlresolvers import reverse
from django.views import generic

from athletes.models import Sport, League, Division, Team, Athlete

def index(request):
	sports = Sport.objects.all()
	return render_to_response('athletes/index.html', {'sports': sports})