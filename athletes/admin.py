from django.contrib import admin
from athletes.models import Sport, League, Division, Team, Athlete

class AthleteAdmin(admin.ModelAdmin):
	list_display = ('__str__', 'team', 'position', 'number', 'status')
	search_fields = ('first_name', 'last_name', 'team__name')

class LeagueAdmin(admin.ModelAdmin):
	list_display = ('name', 'sport')

class DivisionAdmin(admin.ModelAdmin):
	list_display = ('name', 'league', 'sport')

class TeamAdmin(admin.ModelAdmin):
	list_display = ('name', 'division', 'league', 'sport')
	search_fields = ('name',)

admin.site.register(Sport)
admin.site.register(League, LeagueAdmin)
admin.site.register(Division, DivisionAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Athlete, AthleteAdmin)