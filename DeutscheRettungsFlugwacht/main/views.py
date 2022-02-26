from django.shortcuts import render
#from django.http import HttpResponse
from .models import Notverfahren_Flug, Notverfahren_Medizin
import random, json
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
    
    context = {
        "js_list_Notverfahren_Flug" : json.dumps(js_list_Notverfahren_Flug),
        "js_list_Notverfahren_Medizin" : json.dumps(js_list_Notverfahren_Medizin),
    }
    
    return render(response, "main/test.html", context)
