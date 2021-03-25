from rest_framework import generics
from rest_framework.response import Response
from .serializers import JobSerializer
from rest_framework.permissions import AllowAny    
from .models import Job



class JobsIndex(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = (AllowAny,)
