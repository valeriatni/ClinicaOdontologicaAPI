from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..models.appointment import Appointment
from ..serializers.appointment_serializer import AppointmentSerializer, AppointmentDetailSerializer


#class AppointmentViewSet(viewsets.ModelViewSet):
  #  queryset = Appointment.objects.select_related('patient', 'specialist').all()
   # permission_classes = [AllowAny]

    #def get_serializer_class(self):
     #   if self.action == 'retrieve':
      #      return AppointmentDetailSerializer
       # return AppointmentSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.select_related('patient', 'specialist').all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return AppointmentDetailSerializer
        return AppointmentSerializer