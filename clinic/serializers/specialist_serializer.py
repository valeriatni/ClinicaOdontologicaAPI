from rest_framework import serializers
from ..models.specialist import Specialist
from .specialty_serializer import SpecialtySerializer


class SpecialistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialist
        fields = '__all__'


class SpecialistDetailSerializer(SpecialistSerializer):
    specialty = SpecialtySerializer(read_only=True)

    class Meta(SpecialistSerializer.Meta):
        fields = '__all__' 