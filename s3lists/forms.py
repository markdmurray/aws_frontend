from django.forms import ModelForm, Textarea
from django import forms
from .models import ListRegions, TextUpload

class ListRegionsForm(ModelForm):
    class Meta:
        model = ListRegions
        fields = ['regions']

class TextRegionsForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()

