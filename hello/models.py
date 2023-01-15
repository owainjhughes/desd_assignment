from django.db import models
from django.utils import timezone

class LogMessage(models.Model):
    message = models.CharField(max_length=300)
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"
    #migraate database

class Movie(models.Model):
    name = models.CharField(max_length=100)
    rating = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class Screening(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seats_available = models.IntegerField()
    def __str__(self):
        return self.seats_available