from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class userRegistration(UserCreationForm): 

    email = forms.EmailField(required=True)

    phone = forms.IntegerField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone']