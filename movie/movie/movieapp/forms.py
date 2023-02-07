from django import forms
from .models import Movie


class Edit(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'description', 'year', 'image']
