from django.urls import path
from .views import JobList, JobDetail

app_name = 'homeservice_api'

urlpatterns = [
    path('<int:pk>/', JobDetail.as_view(), name='detailcreate'),
    path('', JobList.as_view(), name='listcreate'),
]
