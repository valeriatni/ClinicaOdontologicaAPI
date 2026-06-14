from rest_framework import serializers
from ..models.patient import Patient


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class PatientDetailSerializer(PatientSerializer):
    class Meta(PatientSerializer.Meta):
        fields = '__all__'