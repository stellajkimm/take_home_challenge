from django.contrib import admin
from athletes.models import Sport, League, Division, Team, Athlete

class AthleteAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'team', 'position', 'number', 'status')

class LeagueAdmin(admin.ModelAdmin):
	list_display = ('name', 'sport')

class DivisionAdmin(admin.ModelAdmin):
	list_display = ('name', 'league', 'sport')

class TeamAdmin(admin.ModelAdmin):
	list_display = ('name', 'division', 'league', 'sport')

admin.site.register(Sport)
admin.site.register(League, LeagueAdmin)
admin.site.register(Division, DivisionAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Athlete, AthleteAdmin)