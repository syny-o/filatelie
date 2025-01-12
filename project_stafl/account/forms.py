from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm

from .models import Profile 



class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'floatingInputValue',
            'placeholder': 'Uživatelské jméno',
        })
    )
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'id': 'floatingPassword',
            'placeholder': 'Heslo',
        })
    )





class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label='Heslo',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Zadejte heslo',
            'id': 'passwordInput'
        })
    )
    password2 = forms.CharField(
        label='Heslo znovu',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Zadejte heslo znovu',
            'id': 'password2Input'
        })
    )

    class Meta:
        model = get_user_model()
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Zadejte uživatelské jméno',
                'id': 'usernameInput'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Zadejte e-mail',
                'id': 'emailInput'
            }),
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd.get('password') != cd.get('password2'):
            raise forms.ValidationError('Hesla se neshodují.')
        return cd.get('password2')




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
