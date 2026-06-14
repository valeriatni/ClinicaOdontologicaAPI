from django.shortcuts import render, redirect

from clinic.models.procedure import Procedure

from django.contrib import messages


# LIST
def procedure_list(request):

    procedures = Procedure.objects.all()

    return render(
        request,
        "procedures/list.html",
        {
            "procedures": procedures
        }
    )


# CREATE
def procedure_create(request):

    if request.method == "POST":

        try:

            Procedure.objects.create(

                name=request.POST.get("name"),

                description=request.POST.get(
                    "description"
                ),

                base_price=request.POST.get(
                    "base_price"
                ),
            )

            messages.success(
                request,
                "Procedimiento registrado"
            )

            return redirect("procedure_list")

        except Exception as e:

            messages.error(
                request,
                f"Error: {str(e)}"
            )

            return redirect("procedure_create")

    return render(
        request,
        "procedures/form.html"
    )


# EDIT
def procedure_edit(request, id):

    procedure = Procedure.objects.get(id=id)

    if request.method == "POST":

        procedure.name = request.POST.get(
            "name"
        )

        procedure.description = request.POST.get(
            "description"
        )

        procedure.base_price = request.POST.get(
            "base_price"
        )

        procedure.save()

        messages.success(
            request,
            "Procedimiento actualizado"
        )

        return redirect("procedure_list")

    return render(
        request,
        "procedures/form.html",
        {
            "procedure": procedure
        }
    )


# DELETE LOGICO
def procedure_delete(request, id):

    procedure = Procedure.objects.get(id=id)

    procedure.is_active = False

    procedure.save()

    messages.success(
        request,
        "Procedimiento desactivado"
    )

    return redirect("procedure_list")


# ACTIVATE
def procedure_activate(request, id):

    procedure = Procedure.objects.get(id=id)

    procedure.is_active = True

    procedure.save()

    messages.success(
        request,
        "Procedimiento activado"
    )

    return redirect("procedure_list")