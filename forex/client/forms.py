from django import forms
from django.forms import ModelForm
from .models import *


class clientForm(forms.ModelForm):
    class Meta :
        model = client
        fields = "__all__"

class virtual_private_serverForm(forms.ModelForm):
    class Meta:
        model  =virtual_private_server
        fields = "__all__"

class account_masterForm(forms.ModelForm):
    class Meta:
        model = account_master
        fields = "__all__"
    
class profit_detailsForm(forms.ModelForm):
    class Meta :
        model = profit_details
        fields = ['account_number','entry_date','profit']

class brokerForm(forms.ModelForm):
    class Meta :
        model = broker
        fields = "__all__"