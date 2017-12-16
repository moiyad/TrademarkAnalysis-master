from django import forms
from .models import Trademark

from django import forms


class TrademarkForm(forms.ModelForm):
    class Meta():
        model = Trademark
        fields = ('name', 'image', 'goodsand_services', 'owner_name',)
