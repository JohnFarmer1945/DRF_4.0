from django.db import models

# Create your models here.
class Notverfahren_Flug(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Notverfahren_Medizin(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name        


class Tagesaufgabe(models.Model):
    tag = models.CharField(max_length=50, default="Montag")
    flight_task_day = models.CharField(max_length=100)
    flight_task_night = models.CharField(max_length=100)
    med_task_day = models.CharField(max_length=100)
    med_task_night = models.CharField(max_length=100)
    def __str__(self):
        return self.tag    