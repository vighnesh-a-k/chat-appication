from django import forms
from .models import ChatRoom,Message
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RoomForm(forms.ModelForm):
    class Meta:
        model = ChatRoom
        fields = ['name']

class  messageForm(forms.ModelForm):
    class Meta:
        model=Message
        fields=["content"]
    


class CustomSignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
class loginForm(forms.ModelForm):
    

    class Meta:
        model = User
        fields = ['username', 'password']