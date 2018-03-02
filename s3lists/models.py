from django.db import models
from django import forms

# Create your models here.

region_list = (('ap-southeast-1', 'ap-southeast-2'),
            ('us-east-1', 'us-east-1')
)

class ListRegions(models.Model):
    regions = models.CharField(max_length=20, choices=region_list, default='no region')