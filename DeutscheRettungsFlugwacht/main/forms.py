from django import forms
from pkg_resources import require
from django.forms import ModelForm

from .models import Notverfahren_Medizin

class UpdateForm(forms.Form):
    uniq_id = forms.IntegerField()
    name = forms.CharField(max_length=200)
    del_field = forms.BooleanField(required=False)
    new_field = forms.CharField(max_length=200)
    


