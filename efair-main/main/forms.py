from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms
from .models import *


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('iin','first_name', 'last_name', 'email', 'country', 'city', 'street', 'home_number', 'phone', 'avatar')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'country', 'city', 'street', 'home_number', 'phone', 'avatar')


class OfferSaleCreationForm(forms.ModelForm):
    class Meta:
        model = OfferSale
        fields = ['title', 'image', 'category', 'description', 'manufacturer', 'offer_model', 'amount', 'unit', 'condition_new', 'price', 'country', 'city', 'street', 'home_number']

class OfferSaleChangeForm(forms.ModelForm):
    class Meta:
        model = OfferSale
        fields = ['title', 'image', 'category', 'description', 'manufacturer', 'offer_model', 'amount', 'unit', 'condition_new', 'price', 'country', 'city', 'street', 'home_number']
        
class OfferBuyForm(forms.ModelForm):
    class Meta:
        model = OfferBuy
        fields = ['amount', 'price']