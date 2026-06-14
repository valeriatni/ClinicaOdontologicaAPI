from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..models.patient import Patient
from ..serializers.patient_serializer import PatientSerializer, PatientDetailSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PatientDetailSerializer
        return PatientSerializer