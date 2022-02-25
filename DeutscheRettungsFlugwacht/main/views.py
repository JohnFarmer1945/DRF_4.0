from django.shortcuts import render
#from django.http import HttpResponse
from .models import flightquest
import random, json
# Create your views here.

def home(response):
    all_entries = flightquest.objects.all()
    random_num = random.randint(0, len(all_entries)-1)
    random_flightquest = all_entries[random_num]
    return render(response, "main/home.html", {})
    

def test(response):
    all_entries = flightquest.objects.all()
    js_list = []
    for obj in all_entries:
        js_list.append(obj.name)
    context = {
        "js_list" : json.dumps(js_list),
    }
    return render(response, "main/test.html", context)
