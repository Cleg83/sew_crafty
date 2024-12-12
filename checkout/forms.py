from django import forms
from .models import Order

""" 
Below form and ideas were taken from the Boutique Ado walkthrough project.
There was simply nothing I could improve upon. Yes, I could have kept it very simple
and not gone for the same customisation but it's a nice touch.
"""


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email', 
                  'phone_number', 'address_1', 'address_2', 
                  'town', 'postcode', 'county', 
                  'country')
        
    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postcode',
            'town': 'Town, City or Village etc. ',
            'address_1': 'Address',
            'address_2': 'Address continued',
            'county': 'County or State etc.',
        }

        self.fields['first_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':    
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-formatting'
            self.fields[field].label = False