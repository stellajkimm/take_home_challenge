from django.db import models

class Athlete(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    sport = models.CharField(max_length=200)
    league = models.CharField(max_length=200)
    team = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    picture = models.URLField()