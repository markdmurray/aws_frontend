from django.shortcuts import render
from django.views.generic import CreateView
from .models import ListRegions
from .forms import ListRegionsForm, TextRegionsForm
import boto3
# Create your views here.

"""def index(request):
    return render(
        request,
        'index.html'
    )"""


"""class ListRegionView(CreateView):
    model = ListRegions
    template_name = 'index.html'
    form_class = ListRegionsForm
 """

def check_bucket_in_region(request):
    #region = get_object_or_404()    

    if request.method == 'POST':
        form = ListRegionsForm(request.POST)

        if form.is_valid():
            region = form.cleaned_data['regions']
            client = boto3.client('ec2', region_name=region)
            response = client.describe_instances()
            return render(request, 'index.html', context={'form':form, 'response':response})
    else:
        form = ListRegionsForm
        text = TextRegionsForm
    
    return render(request, 'index.html', context={ 'form':form, 'text':text })
            