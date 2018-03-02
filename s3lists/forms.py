from django.forms import ModelForm
from .models import ListRegions

class ListRegionsForm(ModelForm):
    class Meta:
        model = ListRegions
        fields = ['regions']  