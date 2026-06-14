from django.shortcuts import render, redirect
from clinic.models.specialist import Specialist
from clinic.models.specialty import Specialty
from django.contrib import messages


# LIST
def specialist_list(request):

    specialists = Specialist.objects.all()

    return render(
        request,
        "specialists/list.html",
        {
            "specialists": specialists
        }
    )


# CREATE
def specialist_create(request):

    specialties = Specialty.objects.all()

    if request.method == "POST":

        specialty = Specialty.objects.get(
            id=request.POST.get("specialty")
        )

        Specialist.objects.create(
            first_name=request.POST.get("first_name"),
            last_name=request.POST.get("last_name"),
            cmp=request.POST.get("cmp"),
            phone=request.POST.get("phone"),
            email=request.POST.get("email"),
            specialty=specialty
        )

        messages.success(request, "Especialista registrado")

        return redirect("specialist_list")

    return render(
        request,
        "specialists/form.html",
        {
            "specialties": specialties
        }
    )


# EDIT
def specialist_edit(request, id):

    specialist = Specialist.objects.get(id=id)

    specialties = Specialty.objects.all()

    if request.method == "POST":

        specialist.first_name = request.POST.get("first_name")
        specialist.last_name = request.POST.get("last_name")
        specialist.cmp = request.POST.get("cmp")
        specialist.phone = request.POST.get("phone")
        specialist.email = request.POST.get("email")

        specialist.specialty = Specialty.objects.get(
            id=request.POST.get("specialty")
        )

        specialist.save()

        messages.success(request, "Especialista actualizado")

        return redirect("specialist_list")

    return render(
        request,
        "specialists/edit.html",
        {
            "specialist": specialist,
            "specialties": specialties
        }
    )


# DELETE -> desactivar
def specialist_delete(request, id):

    specialist = Specialist.objects.get(id=id)

    specialist.is_active = False

    specialist.save()

    messages.success(request, "Especialista desactivado")

    return redirect("specialist_list")


# ACTIVATE
def specialist_activate(request, id):

    specialist = Specialist.objects.get(id=id)

    specialist.is_active = True

    specialist.save()

    messages.success(request, "Especialista activado")

    return redirect("specialist_list")