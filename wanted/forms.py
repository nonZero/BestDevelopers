from django import forms

from . import models


class ContactUsForm(forms.Form):
    subject = forms.CharField(max_length=200)
    content = forms.CharField(max_length=1000,
                              widget=forms.Textarea())
    email = forms.EmailField()
    is_important = forms.BooleanField()


class AdForm(forms.ModelForm):
    class Meta:
        model = models.Ad
        exclude = ()