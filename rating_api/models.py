from django.db import models

# Create your models here.


class Rating(models.Model):
    evaluation = models.IntegerField()
    servicePlace = models.TextField()
    comments = models.TextField()
    date = models.DateField(auto_now_add=True)