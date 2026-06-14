from rest_framework import serializers
from ..models.payment import Payment
from .budget_serializer import BudgetNestedSerializer
from .appointment_serializer import AppointmentDetailSerializer


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class PaymentDetailSerializer(PaymentSerializer):
    budget = BudgetNestedSerializer(read_only=True)
    appointment = AppointmentDetailSerializer(read_only=True)

    class Meta(PaymentSerializer.Meta):
        fields = '__all__'