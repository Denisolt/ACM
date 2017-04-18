from django import forms
from .models import User, Competition

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('name', 'major', 'year', 'email',)

class UploadFileForm(forms.ModelForm):
    
    class Meta:
    	model = Competition
    	fields = ('team', 'email', 'member1', 'member2', 'member3', 'submission')