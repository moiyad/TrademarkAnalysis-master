from .models import Trademark
from django import forms


class TrademarkForm(forms.ModelForm):
    class Meta():
        model = Trademark
        fields = ('name', 'Product', 'vienna', 'image', 'owner_name','description',)
