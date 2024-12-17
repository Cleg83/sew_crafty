from django import forms
from .models import UserProfile

""" 
Below form and ideas were taken from the Boutique Ado walkthrough project.
There was simply nothing I could improve upon. Yes, I could have kept it very simple
and not gone for the same customisation but it's a nice touch.
"""


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)
        
    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postcode',
            'default_town': 'Town, City or Village etc. ',
            'default_address_1': 'Address',
            'default_address_2': 'Address continued',
            'default_county': 'County or State etc.',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':    
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-formatting'
            self.fields[field].label = False