from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class userRegistration(UserCreationForm): 

    username= forms.CharField(min_length=5, max_length=50, required=True)

    email = forms.EmailField(required=True)

    phone = forms.IntegerField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone']