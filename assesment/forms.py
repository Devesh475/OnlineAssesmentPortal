from django import forms
from .models import question,questionPaper

class questionForm(forms.ModelForm):
    class Meta:
        model = question
        fields = '__all__'

        widgets = {
            "Question": forms.TextInput(attrs={'class':'form-control'}),
            "A": forms.TextInput(attrs={'class':'form-control'}),
            "B": forms.TextInput(attrs={'class':'form-control'}),
            "C": forms.TextInput(attrs={'class':'form-control'}),
            "D": forms.TextInput(attrs={'class':'form-control'})
        }

CHOICES = (('A','AB'))

class questionPaperForm(forms.ModelForm):
    class Meta:
        model = questionPaper
        fields = ['users','title', 'questionList']

        widgets = {
            "users": forms.CheckboxSelectMultiple(),
            "title": forms.TextInput(attrs={'class':'form-control'}),
            "questionList": forms.CheckboxSelectMultiple()
        }