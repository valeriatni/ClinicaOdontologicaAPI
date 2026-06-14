from django.shortcuts import render, redirect
from clinic.models.specialty import Specialty
from django.contrib import messages


# READ
def specialty_list(request):

    specialties = Specialty.objects.all()

    return render(
        request,
        "specialties/list.html",
        {
            "specialties": specialties
        }
    )


# CREATE
def specialty_create(request):

    if request.method == "POST":

        Specialty.objects.create(
            name=request.POST.get("name"),
            description=request.POST.get("description"),
        )

        messages.success(request, "Especialidad creada")
        return redirect("specialty_list")

    return render(request, "specialties/form.html")


# UPDATE
def specialty_edit(request, id):

    specialty = Specialty.objects.get(id=id)

    if request.method == "POST":

        specialty.name = request.POST.get("name")
        specialty.description = request.POST.get("description")

        specialty.save()

        messages.success(request, "Especialidad actualizada")

        return redirect("specialty_list")

    return render(
        request,
        "specialties/edit.html",
        {
            "specialty": specialty
        }
    )


# DESACTIVAR
def specialty_delete(request, id):

    specialty = Specialty.objects.get(id=id)

    specialty.is_active = False
    specialty.save()

    messages.success(request, "Especialidad desactivada")

    return redirect("specialty_list")


# ACTIVAR
def specialty_activate(request, id):

    specialty = Specialty.objects.get(id=id)

    specialty.is_active = True
    specialty.save()

    messages.success(request, "Especialidad activada")

    return redirect("specialty_list")