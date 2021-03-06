from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class createUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

        widgets = {
            "username": forms.TextInput(attrs={'class':'form-control'}),
            "email": forms.TextInput(attrs={'class':'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(createUser, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'