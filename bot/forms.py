from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):

    class Mets:
        model = Profile
        fields = ('external_name', 'name')
        widgets = {
            'name': forms.TextInput,  
        }