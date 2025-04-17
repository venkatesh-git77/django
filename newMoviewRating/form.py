from django import forms
from .models import MoviewRating

class MovieForm(forms.ModelForm):
    class Meta:
        model = MoviewRating
        fields = '__all__'