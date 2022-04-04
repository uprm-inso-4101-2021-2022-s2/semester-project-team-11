from rest_framework import generics
from homeservice.models import Job
from .serializers import JobSerializer

class JobList(generics.ListCreateAPIView):
    queryset = Job.jobobjects.all()
    serializer_class = JobSerializer

class JobDetail(generics.RetrieveDestroyAPIView):
    queryset = Job.objects.all() #Job.jobobjects.all() ??
    serializer_class = JobSerializer