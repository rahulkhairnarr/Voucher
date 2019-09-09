from django import forms
from .models import Voucher


class VoucherForm(forms.Form):
    """ This Class Create UI for Form from Model """

    # Discount code used for taking input from user
    discount_code = forms.CharField(label='', required=True, widget=forms.TextInput(
        attrs={
            'class': 'input-field col s8',
            'id': 'discount_code'
        }
    ))
