from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Notverfahren_Flug, Notverfahren_Medizin, Tagesaufgabe
import random, json, datetime
from django.contrib import messages 

from .forms import NameForm, ContactForm, UpdateForm

# Create your views here.

def home(response):
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

    return render(response, "main/home.html", context)



def notverfahren(request):
    UpdateForm.base_fields ["name"].widget.attrs ["size"] = "50"
    if request.method == 'POST':
        form = UpdateForm(request.POST)
        if form.is_valid():
            del_field = form.cleaned_data["del_field"]
            new_name = form.cleaned_data['name']
            uniq_id = form.cleaned_data['uniq_id']
            new_field = form.cleaned_data['new_field']
            x = Notverfahren_Medizin.objects.get(pk=uniq_id)
            if new_field != "New Entry":
                new_entry = Notverfahren_Medizin(name=new_field)
                messages.success(request, "New entry saved in databank." )
                new_entry.save()
                return redirect('notverfahren')
            elif del_field == True:
                x.delete()
                messages.success(request, "Entry deleted." )
                return redirect('notverfahren')
            elif x.name != new_name:
                x.name = new_name
                x.save()
                messages.success(request, "Entry changed." )
                return redirect('notverfahren')
            else:
                messages.error(request, "Identical Entry. Entry NOT changed." )
                return redirect('notverfahren')
        


    else:
        objects = Notverfahren_Medizin.objects.all()
        form_list = []
        for obj in objects:
            form = UpdateForm(initial={
                'name' : obj.name, 
                'uniq_id' : obj.id})
            form_list.append(form)
        new_entry_form = UpdateForm(initial={'new_field' : 'New Entry'})
        context = {
            'form_list': form_list,
            'new_entry_form' : new_entry_form}
            
        
    return render(request, "main/notverfahren.html", context)



def form_test(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponse("<h1> THX </h1>")
    else:
        form = NameForm()

    context = {'form' : form}
    return render(request, "main/form_test.html", context)


def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return HttpResponse("<h1> THX </h1>")
    else: 
        form = ContactForm()
    context = {'form' : form}
    return render(request, "main/contact_form.html", context)


