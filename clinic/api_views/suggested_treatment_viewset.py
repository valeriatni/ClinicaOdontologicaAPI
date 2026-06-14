from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


from ..models.suggested_treatment import SuggestedTreatment
from ..serializers.suggested_treatment_serializer import (
    SuggestedTreatmentSerializer,
    SuggestedTreatmentDetailSerializer,
)


class SuggestedTreatmentViewSet(viewsets.ModelViewSet):
    queryset = SuggestedTreatment.objects.select_related(
        'medical_record',
        'medical_record__patient',
        'specialist',
        'specialist__specialty'
    ).all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return SuggestedTreatmentDetailSerializer
        return SuggestedTreatmentSerializer