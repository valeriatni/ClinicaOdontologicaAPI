from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..models.budget import Budget
from ..serializers.budget_serializer import BudgetSerializer, BudgetNestedSerializer


class BudgetViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.select_related(
        'patient',
        'suggested_treatment',
        'suggested_treatment__medical_record',
        'suggested_treatment__medical_record__patient',
        'suggested_treatment__specialist',
        'suggested_treatment__specialist__specialty'
    ).prefetch_related('budgetdetail_set__procedure').all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return BudgetNestedSerializer
        return BudgetSerializer
    