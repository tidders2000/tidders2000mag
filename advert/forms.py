from django import forms
from .models import Advert

class advert_form(forms.ModelForm):
    class Meta:
         model = Advert
         fields = ('business_name','info','contact_email','contact_telephone','slug','advert_image',)
         