from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    phone = forms.CharField(max_length=15)  # Add phone number field
    accepted_terms = forms.BooleanField()  # Add accepted terms field
