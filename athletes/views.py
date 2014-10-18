from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

from athletes.models import Sport, League, Division, Team, Athlete

def index(request):
	return HttpResponse('The Main Page')