from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..models.budget_detail import BudgetDetail
from ..serializers.budget_detail_serializer import BudgetItemSerializer, BudgetItemNestedSerializer


class BudgetDetailViewSet(viewsets.ModelViewSet):
    queryset = BudgetDetail.objects.select_related('budget', 'procedure').all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return BudgetItemNestedSerializer
        return BudgetItemSerializer