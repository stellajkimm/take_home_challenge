from django.contrib import admin
from athletes.models import Sport, League, Division, Team, Athlete

admin.site.register(Sport)
admin.site.register(League)
admin.site.register(Division)
admin.site.register(Team)
admin.site.register(Athlete)