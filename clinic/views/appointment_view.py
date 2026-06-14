from django.shortcuts import render, redirect
from clinic.models.appointment import Appointment
from clinic.models.patient import Patient
from clinic.models.specialist import Specialist

from django.contrib import messages


# LIST
def appointment_list(request):

    appointments = Appointment.objects.all()

    return render(
        request,
        "appointments/list.html",
        {
            "appointments": appointments
        }
    )


# CREATE
def appointment_create(request):

    patients = Patient.objects.filter(is_active=True)
    specialists = Specialist.objects.filter(is_active=True)

    if request.method == "POST":

        try:

            Appointment.objects.create(

                patient_id=request.POST.get("patient_id"),

                specialist_id=request.POST.get("specialist_id"),

                appointment_date=request.POST.get("appointment_date"),

                appointment_time=request.POST.get("appointment_time"),

                reason=request.POST.get("reason"),

                appointment_status=request.POST.get("appointment_status"),
            )

            messages.success(
                request,
                "Cita registrada correctamente"
            )

            return redirect("appointment_list")

        except Exception as e:

            messages.error(
                request,
                f"Error: {str(e)}"
            )

            return redirect("appointment_create")

    return render(
        request,
        "appointments/form.html",
        {
            "patients": patients,
            "specialists": specialists
        }
    )


# EDIT
def appointment_edit(request, id):

    appointment = Appointment.objects.get(id=id)

    patients = Patient.objects.filter(is_active=True)
    specialists = Specialist.objects.filter(is_active=True)

    if request.method == "POST":

        appointment.patient_id = request.POST.get("patient_id")

        appointment.specialist_id = request.POST.get("specialist_id")

        appointment.appointment_date = request.POST.get("appointment_date")

        appointment.appointment_time = request.POST.get("appointment_time")

        appointment.reason = request.POST.get("reason")

        appointment.appointment_status = request.POST.get("appointment_status")

        appointment.save()

        messages.success(
            request,
            "Cita actualizada"
        )

        return redirect("appointment_list")

    return render(
        request,
        "appointments/form.html",
        {
            "appointment": appointment,
            "patients": patients,
            "specialists": specialists
        }
    )


# CANCEL
def appointment_cancel(request, id):

    appointment = Appointment.objects.get(id=id)

    appointment.appointment_status = "Cancelled"

    appointment.save()

    messages.success(
        request,
        "Cita cancelada"
    )

    return redirect("appointment_list")