from django import forms
from website.models import contact,newsletter

class contactForm(forms.ModelForm):

    class Meta:
        model=contact
        fields='__all__'

class newsletterForm(forms.ModelForm):

    class Meta:
        model=newsletter
        fields='__all__'