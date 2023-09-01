from django import forms
from .models import BidDetail, Post


class BidForm(forms.ModelForm):
    class Meta:
        model = BidDetail
        fields = ['customer_bid']
