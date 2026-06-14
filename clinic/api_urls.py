from rest_framework.routers import DefaultRouter
from .api_views import (
    PatientViewSet,
    SpecialtyViewSet,
    SpecialistViewSet,
    AppointmentViewSet,
    MedicalRecordViewSet,
    ProcedureViewSet,
    SuggestedTreatmentViewSet,
    BudgetViewSet,
    BudgetDetailViewSet,
    PaymentViewSet,
)

router = DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patient')
router.register(r'specialties', SpecialtyViewSet, basename='specialty')
router.register(r'specialists', SpecialistViewSet, basename='specialist')
router.register(r'appointments', AppointmentViewSet, basename='appointment')
router.register(r'medical-records', MedicalRecordViewSet, basename='medical-record')
router.register(r'procedures', ProcedureViewSet, basename='procedure')
router.register(r'suggested-treatments', SuggestedTreatmentViewSet, basename='suggested-treatment')
router.register(r'budgets', BudgetViewSet, basename='budget')
router.register(r'budget-details', BudgetDetailViewSet, basename='budget-detail')
router.register(r'payments', PaymentViewSet, basename='payment')

urlpatterns = router.urls