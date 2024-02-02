from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    text = forms.CharField(max_length=255, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Comment kiriting', 'style': "height: 100px"}
    ))
    class Meta:
        model = Comment
        fields = ['text']

class CreateUserForm(UserCreationForm):
    username = forms.CharField(max_length=255, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control form-icon-input', 'placeholder': 'username', 'type': 'text'}
    ))
    first_name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control form-icon-input', 'placeholder': 'Ismini kiriting', 'type': 'text'}
    ))
    last_name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control form-icon-input', 'placeholder': 'Familyani kiriting', 'type': 'text'}
    ))
    password1 = forms.CharField(max_length=255, required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control form-icon-input', 'placeholder': 'Parolni kiriting', 'type': 'password'}
    ))
    password2 = forms.CharField(max_length=255, required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control form-icon-input', 'placeholder': 'Parolni Tastiqlang', 'type': 'password'}
    ))

    class Meta(UserCreationForm):
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'password1', 'password2']
        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control form-icon-input', 'placeholder': 'username', 'type': 'text'}
    ))
    password = forms.CharField(max_length=255, required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control form-icon-input', 'placeholder': 'Parolni kiriting', 'type': 'password'}
    ))
