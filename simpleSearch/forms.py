from django import forms
from simpleSearch.models import TrademarkModel


class TrademarkSearchForm(forms.ModelForm):
    class Meta:
        model = TrademarkModel
        fields = ('Name',)
