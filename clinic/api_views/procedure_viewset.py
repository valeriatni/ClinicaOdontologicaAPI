from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


from ..models.procedure import Procedure
from ..serializers.procedure_serializer import ProcedureSerializer


class ProcedureViewSet(viewsets.ModelViewSet):
    queryset = Procedure.objects.all()
    serializer_class = ProcedureSerializer
    permission_classes = [IsAuthenticated]