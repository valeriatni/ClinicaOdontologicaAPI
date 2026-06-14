from rest_framework import serializers
from ..models.budget import Budget
from .patient_serializer import PatientSerializer
from .suggested_treatment_serializer import SuggestedTreatmentDetailSerializer


class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = '__all__'


class BudgetNestedSerializer(BudgetSerializer):
    patient = PatientSerializer(read_only=True)
    suggested_treatment = SuggestedTreatmentDetailSerializer(read_only=True)
    budget_details = serializers.SerializerMethodField()

    class Meta(BudgetSerializer.Meta):
        fields = '__all__'

    def get_budget_details(self, obj):
        from .budget_detail_serializer import BudgetItemSerializer
        return BudgetItemSerializer(obj.budgetdetail_set.all(), many=True).data