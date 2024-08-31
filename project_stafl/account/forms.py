from django import forms
from django.contrib.auth import get_user_model

from .models import Profile 


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Heslo', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Heslo znovu', widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email']

    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Hesla se neshodují.')
        return cd['password2']
    

class UserEditForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }
    

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['date_of_birth', 'photo']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
        }
