from django.test import TestCase

# Create your tests here.
from django import forms
from .models import Cliente

class ClientForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__' 