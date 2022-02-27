from django.shortcuts import render
#from django.http import HttpResponse
from .models import Notverfahren_Flug, Notverfahren_Medizin, Tagesaufgabe
import random, json, datetime

# Create your views here.

def home(response):
    all_ = flightquest.objects.all()
    random_num = random.randint(0, len(all_entries)-1)
    random_flightquest = all_entries[random_num]
    return render(response, "main/home.html", {})
    

def test(response):
    all_obj_Notverfahren_Flug = Notverfahren_Flug.objects.all()
    js_list_Notverfahren_Flug = []
    for obj in all_obj_Notverfahren_Flug:
        js_list_Notverfahren_Flug.append(obj.name)
    
    all_obj_Notverfahren_Medizin = Notverfahren_Medizin.objects.all()
    js_list_Notverfahren_Medizin = []
    for obj in all_obj_Notverfahren_Medizin:
        js_list_Notverfahren_Medizin.append(obj.name)
    
    date = datetime.datetime.now()
    day_now = date.strftime("%A")
    obj_tagesaufgabe_flug_med = Tagesaufgabe.objects.get(tag=day_now)

    context = {
        "js_list_Notverfahren_Flug" : json.dumps(js_list_Notverfahren_Flug),
        "js_list_Notverfahren_Medizin" : json.dumps(js_list_Notverfahren_Medizin),
        "flight_task_day" : obj_tagesaufgabe_flug_med.flight_task_day,
        "flight_task_night" : obj_tagesaufgabe_flug_med.flight_task_night, 
        "med_task_day" : obj_tagesaufgabe_flug_med.med_task_day,
        "med_task_night" : obj_tagesaufgabe_flug_med.med_task_night,
    }

    return render(response, "main/test.html", context)
