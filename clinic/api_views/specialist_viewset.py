from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..models.specialist import Specialist
from ..serializers.specialist_serializer import SpecialistSerializer, SpecialistDetailSerializer


class SpecialistViewSet(viewsets.ModelViewSet):
    queryset = Specialist.objects.select_related('specialty').all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return SpecialistDetailSerializer
        return SpecialistSerializer