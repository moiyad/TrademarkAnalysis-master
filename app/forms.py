from django import forms
from .models import Trademark

from django import forms


#class ContactForm(forms.Form):
 #   full_name=forms.CharField()
  #  email =forms.EmailField()
   # meassage=forms.CharField()
           
class TrademarkForm(forms.ModelForm):
    class Meta():
        model = Trademark
        fields = ('name','image','goodsand_services','owner_name',)