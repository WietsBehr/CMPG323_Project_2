from django import forms
from .models import Photo

class PhotoForm(forms.ModelForm):
    class Meta:
        model=Photo
        fields=["title", "location", "image"]

class EditForm(forms.ModelForm):
    class Meta:
        model=Photo
        fields=["title", "location", 'image']