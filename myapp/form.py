from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

        self.fields['business_type'].empty_label = "Select an option..."

    class Meta:
        model = Contact
        fields = "__all__"  

        widgets = {
            'business_type': forms.Select(choices=Contact.bu_type,attrs={'class':'form-control fmselect'}),
            'business_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Business Name'}),
            'established_year': forms.NumberInput(attrs={'class':'form-control'}),
            'name': forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Name'}),
            'phone': forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Phone Number'}),
            'title': forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Title'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder': 'Enter Email Address'}),
            'address': forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Address'}),
            'country':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Country'}),
            'state':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter State'}),
            'city':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter City'}),
            'zip':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Zip code'}),
            'website': forms.URLInput(attrs={'class':'form-control','placeholder': 'Enter Website URL'})
        }
