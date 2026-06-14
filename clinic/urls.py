from django.urls import path
from clinic.views import *

urlpatterns = [
    path('', home, name='home'),

    # SPECIALTIES
    path('specialties/', specialty_list, name='specialty_list'),
    path('specialties/create/', specialty_create, name='specialty_create'),
    path('specialties/edit/<int:id>/', specialty_edit, name='specialty_edit'),
    path('specialties/delete/<int:id>/', specialty_delete, name='specialty_delete'),
    path('specialties/activate/<int:id>/', specialty_activate, name='specialty_activate'),

    path('specialists/',specialist_list,name='specialist_list'),
    path('specialists/create/',specialist_create,name='specialist_create'),
    path('specialists/edit/<int:id>/',specialist_edit,name='specialist_edit'),
    path('specialists/delete/<int:id>/',specialist_delete,name='specialist_delete'),
    path('specialists/activate/<int:id>/',specialist_activate,name='specialist_activate'),
        
    # PATIENTS
    path('patients/', patient_list, name='patient_list'),
    path('patients/create/', patient_create, name='patient_create'),
    path('patients/edit/<int:id>/', patient_update, name='patient_update'),
    path('patients/delete/<int:id>/', patient_delete, name='patient_delete'),
    path('patients/activate/<int:id>/', patient_activate, name='patient_activate'),

    # MEDICAL RECORDS
    path('medical-records/',medical_record_list,name='medical_record_list'),
    path('medical-records/create/',medical_record_create,name='medical_record_create'),
    path('medical-records/edit/<int:id>/',medical_record_edit,name='medical_record_edit'),
    path('medical-records/delete/<int:id>/',medical_record_delete,name='medical_record_delete'),
    path('medical-records/activate/<int:id>/',medical_record_activate,name='medical_record_activate'),
   
    # APPOINTMENTS
    path('appointments/',appointment_list,name='appointment_list'),
    path('appointments/create/',appointment_create,name='appointment_create'),
    path('appointments/edit/<int:id>/',appointment_edit,name='appointment_edit'),
    path('appointments/cancel/<int:id>/',appointment_cancel,name='appointment_cancel'),

    # SUGGESTED TREATMENT
    path('suggested-treatments/',suggested_treatment_list,name='suggested_treatment_list'),
    path('suggested-treatments/create/',suggested_treatment_create,name='suggested_treatment_create'),
    path('suggested-treatments/edit/<int:id>/',suggested_treatment_edit,name='suggested_treatment_edit'),

    # PROCEDURES
    path('procedures/',procedure_list,name='procedure_list'),
    path('procedures/create/',procedure_create,name='procedure_create'),
    path('procedures/edit/<int:id>/',procedure_edit,name='procedure_edit'),
    path('procedures/delete/<int:id>/',procedure_delete,name='procedure_delete'),
    path('procedures/activate/<int:id>/',procedure_activate,name='procedure_activate'),

    # BUDGETS
    path('budgets/',budget_list,name='budget_list'),
    path('budgets/create/',budget_create,name='budget_create'),
    path('budgets/edit/<int:id>/',budget_edit,name='budget_edit'),

    # BUDGET DETAILS
    path('budget-details/',budget_detail_list,name='budget_detail_list'),
    path('budget-details/create/',budget_detail_create,name='budget_detail_create'),
    path('budget-details/edit/<int:id>/',budget_detail_edit,name='budget_detail_edit'),

    # PAYMENTS
    path('payments/',payment_list,name='payment_list'),
    path('payments/create/',payment_create,name='payment_create'),
    path('payments/edit/<int:id>/',payment_edit,name='payment_edit'),
]