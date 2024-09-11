from django import forms
from website.models import contact,newsletter
from captcha.fields import CaptchaField


class contactForm(forms.ModelForm):
    captcha=CaptchaField()
    
    class Meta:
        model=contact
        fields='__all__'

class newsletterForm(forms.ModelForm):

    class Meta:
        model=newsletter
        fields='__all__'