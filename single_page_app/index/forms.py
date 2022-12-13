from django import forms
from django.forms import ModelForm, Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import DateInput
from . import models


class libraryForm(ModelForm):
    class Meta:
        model = models.Library
        exclude = []


class emptyEventForm(ModelForm):
    class Meta:
        model = models.Event
        exclude = []
        widgets = {
            'starttime': DateInput(attrs={'type': 'date'}),
            'endtime': DateInput(attrs={'type': 'date'})

        }