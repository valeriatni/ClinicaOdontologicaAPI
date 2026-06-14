from rest_framework import serializers
from ..models.medical_record import MedicalRecord
from .patient_serializer import PatientSerializer


class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = '__all__'


class MedicalRecordDetailSerializer(MedicalRecordSerializer):
    patient = PatientSerializer(read_only=True)

    class Meta(MedicalRecordSerializer.Meta):
        fields = '__all__'