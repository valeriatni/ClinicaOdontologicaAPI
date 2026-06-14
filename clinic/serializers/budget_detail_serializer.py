from rest_framework import serializers
from ..models.budget_detail import BudgetDetail
from .budget_serializer import BudgetSerializer
from .procedure_serializer import ProcedureSerializer


class BudgetItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetDetail
        fields = '__all__'


class BudgetItemNestedSerializer(BudgetItemSerializer):
    budget = BudgetSerializer(read_only=True)
    procedure = ProcedureSerializer(read_only=True)

    class Meta(BudgetItemSerializer.Meta):
        fields = '__all__'