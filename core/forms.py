from django import forms
from core.models import Document, Demo


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document',)


class DemoForm(forms.ModelForm):
    class Meta:
        model = Demo
        fields = ('name','image',)
