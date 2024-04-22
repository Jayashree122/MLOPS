# models.py
from django.db import models

class React(models.Model):
    Overall_rank = models.CharField(max_length=200)
    Score = models.CharField(max_length=200)
    Social_support = models.CharField(max_length=200)
    Healthy_life_expectancy = models.CharField(max_length=200)
    Freedom_to_make_life_choices = models.CharField(max_length=200)
    Generosity = models.CharField(max_length=200)
    Perceptions_of_corruption = models.CharField(max_length=200)

  
