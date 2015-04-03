__author__ = 'sparky'
from django import forms


class EForm(forms.Form):


    age = forms.IntegerField()
    name = forms.CharField(max_length=256)
    city = forms.CharField(max_length=256)