from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class JobSeekerRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'job_seeker'
        if commit:
            user.save()
        return user
    
class EmployerRegisterForm(UserCreationForm):
    companyname = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['email', 'companyname', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'employer'
        companyname = self.cleaned_data.get('companyname')
        user.username = companyname  
        user.companyname = companyname 
        if commit:
            user.save()
        return user

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )