from email import message
from django import forms
from .models import Create


class CreateToken(forms.ModelForm):
    class Meta:
        model = Create
        fields = ['title', 'discription',
                  'email', 'price', 'benefit', 'upload']
