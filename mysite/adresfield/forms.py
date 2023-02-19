from django import forms
from adresfield.models import Addres

class AddresForm(forms.ModelForm):
    # start_point = forms.CharField(max_length=90, help_text="Enter your location" )
    # target_point = forms.CharField(max_length=90, help_text="Enter where you want to drive")
    # name = forms.CharField(max_length=20, help_text="enter your name")
    # phone_number = forms.DecimalField(max_digits=10, help_text="number as 0953130240")
    class Meta:
        model = Addres
        fields = ("street_from", "street_to", "name", "phone")

