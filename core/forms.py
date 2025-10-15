from django import forms
from .models import Client, Order

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone', 'company']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['client', 'title', 'description', 'amount', 'status']
