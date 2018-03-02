from django.urls import path
#from s3lists.views import ListRegionView
from . import views

urlpatterns = [
    #path('', ListRegionView.as_view())
    path('', views.check_bucket_in_region, name='index')
]