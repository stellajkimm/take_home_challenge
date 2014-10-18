from django.db import models

class Sport(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class League(models.Model):
    sport = models.ForeignKey(Sport)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Division(models.Model):
    league = models.ForeignKey(League)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def sport(self):
        return self.league.sport

class Team(models.Model):
    division = models.ForeignKey(Division)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def league(self):
        return self.division.league

    def sport(self):
        return self.division.league.sport

class Athlete(models.Model):
    team = models.ForeignKey(Team)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    number = models.CharField(max_length=200)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    def sport(self):
        return self.team.division.league.sport