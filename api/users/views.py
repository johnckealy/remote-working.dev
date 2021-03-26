from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import ProfileSerializer
from .models import Profile


class ProfileDetail(generics.GenericAPIView):

    permission_classes = [ IsAuthenticated ]
    serializer_class = ProfileSerializer

    def get(self, request, *args, **kwargs):
        user = request.user
        try:
            profile_serializer = ProfileSerializer(user.profile)
            return Response(profile_serializer.data)
        except:
            return Response({"include_chips": [], "ignore_chips": []})

    def post(self, request, format=None):

        try:
            profile = Profile.objects.get(user=request.user)
        except:
            profile = Profile.objects.create(user=request.user)
        else:
            profile.include_chips = request.data['includeChips']
            profile.ignore_chips = request.data['ignoreChips']
            profile.save()

        return Response(ProfileSerializer(profile).data)