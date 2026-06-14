from django.shortcuts import render, redirect

from clinic.models.budget_detail import BudgetDetail
from clinic.models.budget import Budget
from clinic.models.procedure import Procedure

from django.contrib import messages


# LIST
def budget_detail_list(request):

    details = BudgetDetail.objects.all()

    return render(
        request,
        "budget_details/list.html",
        {
            "details": details
        }
    )


# CREATE
def budget_detail_create(request):

    budgets = Budget.objects.all()

    procedures = Procedure.objects.filter(
        is_active=True
    )

    if request.method == "POST":

        try:

            quantity = int(
                request.POST.get("quantity")
            )

            unit_price = float(
                request.POST.get("unit_price")
            )

            subtotal = quantity * unit_price

            BudgetDetail.objects.create(

                budget_id=request.POST.get(
                    "budget_id"
                ),

                procedure_id=request.POST.get(
                    "procedure_id"
                ),

                quantity=quantity,

                unit_price=unit_price,

                subtotal=subtotal,

                item_status=request.POST.get(
                    "item_status"
                ),
            )

            messages.success(
                request,
                "Detalle registrado"
            )

            return redirect(
                "budget_detail_list"
            )

        except Exception as e:

            messages.error(
                request,
                f"Error: {str(e)}"
            )

            return redirect(
                "budget_detail_create"
            )

    return render(
        request,
        "budget_details/form.html",
        {
            "budgets": budgets,
            "procedures": procedures
        }
    )


# EDIT
def budget_detail_edit(request, id):

    detail = BudgetDetail.objects.get(id=id)

    budgets = Budget.objects.all()

    procedures = Procedure.objects.filter(
        is_active=True
    )

    if request.method == "POST":

        quantity = int(
            request.POST.get("quantity")
        )

        unit_price = float(
            request.POST.get("unit_price")
        )

        subtotal = quantity * unit_price

        detail.budget_id = request.POST.get(
            "budget_id"
        )

        detail.procedure_id = request.POST.get(
            "procedure_id"
        )

        detail.quantity = quantity

        detail.unit_price = unit_price

        detail.subtotal = subtotal

        detail.item_status = request.POST.get(
            "item_status"
        )

        detail.save()

        messages.success(
            request,
            "Detalle actualizado"
        )

        return redirect(
            "budget_detail_list"
        )

    return render(
        request,
        "budget_details/form.html",
        {
            "detail": detail,
            "budgets": budgets,
            "procedures": procedures
        }
    )