from django import forms
from .models import CustomUser
class Login(forms.Form):
    username = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    password = forms.CharField(
        max_length=200,
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )



class Profile(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username','first_name','last_name','email',)