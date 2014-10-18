from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader, Context
from django.core.urlresolvers import reverse
from django.views import generic

from athletes.models import Sport, League, Division, Team, Athlete

def index(request):
	sports = Sport.objects.all()
	template = loader.get_template('athletes/index.html')
	context = Context({'sports': sports})
	response = template.render(context)
	return HttpResponse(response)