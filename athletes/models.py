from django.db import models

class Sport(models.Model):
    name = models.CharField(max_length=200)

class League(models.Model):
    sport = models.ForeignKey(Sport)
    name = models.CharField(max_length=200)

class Division(models.Model):
    league = models.ForeignKey(League)
    name = models.CharField(max_length=200)

class Team(models.Model):
    division = models.ForeignKey(Division)
    name = models.CharField(max_length=200)

class Athlete(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    sport = models.CharField(max_length=200)
    league = models.CharField(max_length=200)
    team = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    picture = models.URLField()