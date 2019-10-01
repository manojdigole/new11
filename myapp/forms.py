from django import forms
from .models import *


class CalForm(forms.Form):
    valuea = forms.IntegerField()
    Valueb = forms.IntegerField()

class contctform(forms.ModelForm):

    class Meta():
        model = Contactdata
        fields = ['name','email','mobile','text']


class HotelForm(forms.ModelForm):


    class Meta:
        model = ImageModel
        fields = ['name','image']