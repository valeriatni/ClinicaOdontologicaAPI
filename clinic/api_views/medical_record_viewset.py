from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..models.medical_record import MedicalRecord
from ..serializers.medical_record_serializer import MedicalRecordSerializer, MedicalRecordDetailSerializer


class MedicalRecordViewSet(viewsets.ModelViewSet):
    queryset = MedicalRecord.objects.select_related('patient').all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return MedicalRecordDetailSerializer
        return MedicalRecordSerializer