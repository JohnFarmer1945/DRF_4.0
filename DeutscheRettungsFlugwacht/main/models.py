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