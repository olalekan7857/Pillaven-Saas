from django import forms 
from .models import Review_message


class ReviewForm(forms.ModelForm):
    name = forms.CharField(max_length = 50, widget=forms.TextInput(attrs={
        'class': 'form-control required', 'name': 'form_name', 'placeholder': 'Enter Name'
    }))

    email = forms.CharField(max_length = 250, widget=forms.EmailInput(attrs={
        'class': 'form-control required email', 'name': 'form_email', 'placeholder': 'Enter Email'
    }))

    subject = forms.CharField(max_length = 250, widget=forms.TextInput(attrs={
        'class': 'form-control required', 'name': 'form_subject', 'placeholder': 'Enter Subject'
    }))

    phone_number = forms.CharField(max_length = 50, widget=forms.TextInput(attrs={
        'class': 'form-control', 'name': 'form_phone', 'placeholder': 'Enter Phone'
    }))

    message = forms.CharField(max_length = 250, widget=forms.Textarea(attrs={
        'class': 'form-control required', 'rows': 7, 'name': 'form_message', 'placeholder': 'Tell us about your project needs or business challenges'
    }))
    
    class Meta:
        model = Review_message
        fields = ['name', 'email','subject','phone_number', 'message']