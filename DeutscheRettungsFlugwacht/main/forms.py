from django import forms
from pkg_resources import require
from django.forms import ModelForm

from .models import Notverfahren_Medizin



class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField
    cc_myself = forms.BooleanField(required=False)


class UpdateForm(forms.Form):
    uniq_id = forms.IntegerField()
    name = forms.CharField(max_length=200)
    del_field = forms.BooleanField(required=False)
    new_field = forms.CharField(max_length=200)
    


