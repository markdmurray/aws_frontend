from django.forms import ModelForm, Textarea
from django import forms
from .models import ListRegions, TextUpload

class ListRegionsForm(ModelForm):# use the modelform when you need to use a model
    class Meta:
        model = ListRegions
        fields = ['regions']

class TextRegionsForm(forms.Form):# use forms class when you don't need a model
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()

class S3UploadForm(forms.Form):
    bucket_name = forms.CharField(max_length=100)
    region = forms.CharField(max_length=100)
