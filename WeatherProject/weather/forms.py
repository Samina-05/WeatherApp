# weather/forms.py

from django import forms

class CityForm(forms.Form):
    name = forms.CharField(label='City', max_length=50)