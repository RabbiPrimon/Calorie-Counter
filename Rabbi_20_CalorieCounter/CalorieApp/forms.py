from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile, DailyConsumption

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'age', 'gender', 'height', 'weight']

class DailyConsumptionForm(forms.ModelForm):
    class Meta:
        model = DailyConsumption
        fields = ['item_name', 'quantity', 'calories']
        widgets = {
            'item_name': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control'}),
            'calories': forms.NumberInput(attrs={'class': 'form-control'}),
        }
