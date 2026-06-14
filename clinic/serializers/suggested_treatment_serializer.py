from rest_framework import serializers
from ..models.suggested_treatment import SuggestedTreatment
from .medical_record_serializer import MedicalRecordSerializer, MedicalRecordDetailSerializer
from .specialist_serializer import SpecialistSerializer, SpecialistDetailSerializer


class SuggestedTreatmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuggestedTreatment
        fields = '__all__'


class SuggestedTreatmentDetailSerializer(SuggestedTreatmentSerializer):
    medical_record = MedicalRecordDetailSerializer(read_only=True)
    specialist = SpecialistDetailSerializer(read_only=True)

    class Meta(SuggestedTreatmentSerializer.Meta):
        fields = '__all__'