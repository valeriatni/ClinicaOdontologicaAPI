from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


from ..models.specialty import Specialty
from ..serializers.specialty_serializer import SpecialtySerializer


class SpecialtyViewSet(viewsets.ModelViewSet):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer
    permission_classes = [IsAuthenticated]