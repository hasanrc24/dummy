from rest_framework.viewsets import ModelViewSet
from DummyApp.models import UserProfile
from DummyApp.serializers import UserProfileSerializer


# Create your views here.
class UserProfileViewSet(ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
