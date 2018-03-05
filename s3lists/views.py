from django.shortcuts import render
from django.views.generic import CreateView
from .models import ListRegions
from .forms import ListRegionsForm, TextRegionsForm, S3UploadForm
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

def create_bucket(request):
    if request.method == 'POST':
        form = S3UploadForm(request.POST)

        if form .is_valid():
            bucket_name = form.cleaned_data['bucket_name']
            region = form.cleaned_data['region']
            client = boto3.client('s3', region_name=region)
            response = client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={
                    'LocationConstraint': region
                },
            )
            success_code = response['ResponseMetadata']    
            return render(request, 's3upload.html', context={ 'form':form, 'response':success_code })
    else:
        form = S3UploadForm 
    
    return render(request,'s3upload.html', context={'form':form})
