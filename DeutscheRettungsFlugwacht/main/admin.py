from django.contrib import admin
from .models import Notverfahren_Flug, Notverfahren_Medizin, Tagesaufgabe

# Register your models here.
@admin.register(Notverfahren_Flug)
class Notverfahren_Flug_Admin(admin.ModelAdmin):
    list_display = ("id", "name")

@admin.register(Notverfahren_Medizin)
class Notverfahren_Medizin_Admin(admin.ModelAdmin):
    list_display = ("id", "name")
    ordering = (["-id"])
    

    
@admin.register(Tagesaufgabe)
class Tagesaufgabe_Admin(admin.ModelAdmin):
    list_display = ("tag", "flight_task_day", "flight_task_night", "med_task_day", "med_task_night")