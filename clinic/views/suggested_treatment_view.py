from django.shortcuts import render, redirect

from clinic.models.suggested_treatment import SuggestedTreatment
from clinic.models.medical_record import MedicalRecord
from clinic.models.specialist import Specialist

from django.contrib import messages


# LIST
def suggested_treatment_list(request):

    treatments = SuggestedTreatment.objects.all()

    return render(
        request,
        "suggested_treatments/list.html",
        {
            "treatments": treatments
        }
    )


# CREATE
def suggested_treatment_create(request):

    medical_records = MedicalRecord.objects.filter(
        is_active=True
    )

    specialists = Specialist.objects.filter(
        is_active=True
    )

    if request.method == "POST":

        try:

            SuggestedTreatment.objects.create(

                medical_record_id=request.POST.get(
                    "medical_record_id"
                ),

                specialist_id=request.POST.get(
                    "specialist_id"
                ),

                diagnosis=request.POST.get(
                    "diagnosis"
                ),

                treatment_description=request.POST.get(
                    "treatment_description"
                ),

                diagnosis_date=request.POST.get(
                    "diagnosis_date"
                ),

                treatment_status=request.POST.get(
                    "treatment_status"
                ),
            )

            messages.success(
                request,
                "Tratamiento registrado"
            )

            return redirect(
                "suggested_treatment_list"
            )

        except Exception as e:

            messages.error(
                request,
                f"Error: {str(e)}"
            )

            return redirect(
                "suggested_treatment_create"
            )

    return render(
        request,
        "suggested_treatments/form.html",
        {
            "medical_records": medical_records,
            "specialists": specialists
        }
    )


# EDIT
def suggested_treatment_edit(request, id):

    treatment = SuggestedTreatment.objects.get(
        id=id
    )

    medical_records = MedicalRecord.objects.filter(
        is_active=True
    )

    specialists = Specialist.objects.filter(
        is_active=True
    )

    if request.method == "POST":

        treatment.medical_record_id = request.POST.get(
            "medical_record_id"
        )

        treatment.specialist_id = request.POST.get(
            "specialist_id"
        )

        treatment.diagnosis = request.POST.get(
            "diagnosis"
        )

        treatment.treatment_description = request.POST.get(
            "treatment_description"
        )

        treatment.diagnosis_date = request.POST.get(
            "diagnosis_date"
        )

        treatment.treatment_status = request.POST.get(
            "treatment_status"
        )

        treatment.save()

        messages.success(
            request,
            "Tratamiento actualizado"
        )

        return redirect(
            "suggested_treatment_list"
        )

    return render(
        request,
        "suggested_treatments/form.html",
        {
            "treatment": treatment,
            "medical_records": medical_records,
            "specialists": specialists
        }
    )