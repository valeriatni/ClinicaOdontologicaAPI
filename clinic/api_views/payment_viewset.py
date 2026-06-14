from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..models.payment import Payment
from ..serializers.payment_serializer import PaymentSerializer, PaymentDetailSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.select_related(
        'budget',
        'budget__patient',
        'budget__suggested_treatment',
        'appointment',
        'appointment__patient',
        'appointment__specialist',
        'appointment__specialist__specialty'
    ).all()
    permission_classes = [IsAuthenticated]
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PaymentDetailSerializer
        return PaymentSerializer