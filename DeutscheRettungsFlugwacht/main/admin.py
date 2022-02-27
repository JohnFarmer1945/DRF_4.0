from django.contrib import admin
from .models import Notverfahren_Flug, Notverfahren_Medizin, Tagesaufgabe

# Register your models here.
admin.site.register(Notverfahren_Flug)
admin.site.register(Notverfahren_Medizin)
admin.site.register(Tagesaufgabe)