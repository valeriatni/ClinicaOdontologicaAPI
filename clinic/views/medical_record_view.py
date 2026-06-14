from django.shortcuts import render, redirect
from clinic.models.medical_record import MedicalRecord
from clinic.models.patient import Patient

from django.contrib import messages


# LIST
def medical_record_list(request):

    medical_records = MedicalRecord.objects.all()

    return render(
        request,
        "medical_records/list.html",
        {
            "medical_records": medical_records
        }
    )


# CREATE
def medical_record_create(request):

    patients = Patient.objects.filter(is_active=True)

    if request.method == "POST":

        try:

            MedicalRecord.objects.create(

                patient_id=request.POST.get("patient_id"),

                medical_history=request.POST.get("medical_history"),

                allergies=request.POST.get("allergies"),

                general_observations=request.POST.get(
                    "general_observations"
                ),
            )

            messages.success(
                request,
                "Historia clínica registrada"
            )

            return redirect("medical_record_list")

        except Exception as e:

            messages.error(
                request,
                f"Error: {str(e)}"
            )

            return redirect("medical_record_create")

    return render(
        request,
        "medical_records/form.html",
        {
            "patients": patients
        }
    )


# EDIT
def medical_record_edit(request, id):

    medical_record = MedicalRecord.objects.get(id=id)

    patients = Patient.objects.filter(is_active=True)

    if request.method == "POST":

        medical_record.patient_id = request.POST.get(
            "patient_id"
        )

        medical_record.medical_history = request.POST.get(
            "medical_history"
        )

        medical_record.allergies = request.POST.get(
            "allergies"
        )

        medical_record.general_observations = request.POST.get(
            "general_observations"
        )

        medical_record.save()

        messages.success(
            request,
            "Historia clínica actualizada"
        )

        return redirect("medical_record_list")

    return render(
        request,
        "medical_records/form.html",
        {
            "medical_record": medical_record,
            "patients": patients
        }
    )


# DELETE LOGICO
def medical_record_delete(request, id):

    medical_record = MedicalRecord.objects.get(id=id)

    medical_record.is_active = False

    medical_record.save()

    messages.success(
        request,
        "Historia clínica desactivada"
    )

    return redirect("medical_record_list")


# ACTIVATE
def medical_record_activate(request, id):

    medical_record = MedicalRecord.objects.get(id=id)

    medical_record.is_active = True

    medical_record.save()

    messages.success(
        request,
        "Historia clínica activada"
    )

    return redirect("medical_record_list")