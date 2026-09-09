from rest_framework import viewsets
from minutes.models import Minutes
from minutes.serializers import MinutesSerializer

class MinutesViewSet(viewsets.ModelViewSet):
    queryset = Minutes.objects.all()
    serializer_class = MinutesSerializer