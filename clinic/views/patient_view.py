from django.shortcuts import render, redirect
from clinic.models.patient import Patient
from django.contrib import messages
from django.db import IntegrityError


# READ
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patients/list.html', {
        'patients': patients    
    })


# CREATE
def patient_create(request):
    if request.method == "POST":
        try:
            Patient.objects.create(
                first_name=request.POST.get("first_name"),
                last_name=request.POST.get("last_name"),
                dni=request.POST.get("dni"),
                phone=request.POST.get("phone"),
                email=request.POST.get("email"),
                birth_date=request.POST.get("birth_date"),
                address=request.POST.get("address"),
            )

            messages.success(request, "Paciente registrado correctamente")
            return redirect("patient_list")

        except IntegrityError:
            messages.error(request, "Ese email ya está registrado")
            return redirect("patient_create")

        except Exception as e:
            messages.error(request, f"Error inesperado: {str(e)}")
            return redirect("patient_create")

    return render(request, "patients/form.html")

def patient_update(request, id):
    patient = Patient.objects.get(id=id)

    if request.method == "POST":
        patient.first_name = request.POST.get("first_name")
        patient.last_name = request.POST.get("last_name")
        patient.dni = request.POST.get("dni")
        patient.phone = request.POST.get("phone")
        patient.email = request.POST.get("email")
        patient.birth_date = request.POST.get("birth_date")
        patient.address = request.POST.get("address")
        patient.save()

        messages.success(request, "Paciente actualizado")
        return redirect("patient_list")

    return render(request, "patients/form.html", {"patient": patient})

def patient_delete(request, id):
    patient = Patient.objects.get(id=id)

    if request.method == "POST":
        patient.is_active = False
        patient.save()

        messages.success(request, "Paciente desactivado")
        return redirect("patient_list")

    return redirect("patient_list")

def patient_activate(request, id):
    patient = Patient.objects.get(id=id)

    if request.method == "POST":
        patient.is_active = True
        patient.save()

        messages.success(request, "Paciente reactivado")
        return redirect("patient_list")

    return redirect("patient_list")