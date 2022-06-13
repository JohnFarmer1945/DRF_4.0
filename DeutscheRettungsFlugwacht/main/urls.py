from django.urls import path
from . import views

urlpatterns =  [
path("", views.home, name="index"),
path("form_test", views.form_test, name="form_test"),
path("contact_form", views.contact_form, name="contact_form"),
path("notverfahren", views.notverfahren, name="notverfahren"),
]