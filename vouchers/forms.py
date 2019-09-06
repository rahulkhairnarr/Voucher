from django import forms
from .models import Voucher

class VoucherForm(forms.Form):
    discount_code = forms.CharField(label='', required=True, widget=forms.TextInput(
        attrs={
            'class': 'input-field col s8',
            'id': 'discount_code'
        }
    ))