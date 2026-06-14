from rest_framework import serializers
from ..models.appointment import Appointment
from .patient_serializer import PatientSerializer
from .specialist_serializer import SpecialistSerializer


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'


class AppointmentDetailSerializer(AppointmentSerializer):
    patient = PatientSerializer(read_only=True)
    specialist = SpecialistSerializer(read_only=True)

    class Meta(AppointmentSerializer.Meta):
        fields = '__all__'