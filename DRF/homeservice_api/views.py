from rest_framework import generics
from homeservice.models import Job
from .serializers import JobSerializer
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAuthenticatedOrReadOnly, IsAdminUser, DjangoModelPermissions

class JobUserWritePermission(BasePermission):
    message = 'Editing can only be done by owner.'

    def has_object_permission(self, request, view, obj):
        # GET, OPTIONS or HEAD
        if request.method in SAFE_METHODS:
            return True

        return obj.owner == request.user
        

        # return super().has_object_permission(request, view, obj)

class JobList(generics.ListCreateAPIView):
    # Permits only to read when not logged in
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Job.jobobjects.all()
    serializer_class = JobSerializer

class JobDetail(generics.RetrieveUpdateDestroyAPIView, JobUserWritePermission):
    permission_classes = [JobUserWritePermission]
    queryset = Job.objects.all() #Job.jobobjects.all() ??
    serializer_class = JobSerializer