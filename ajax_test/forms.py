from django import forms
from .models import Images


class DemoForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ('name', 'image',)
