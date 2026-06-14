from django.shortcuts import render, redirect

from clinic.models.budget import Budget
from clinic.models.patient import Patient
from clinic.models.suggested_treatment import SuggestedTreatment

from django.contrib import messages


# LIST
def budget_list(request):

    budgets = Budget.objects.all()

    return render(
        request,
        "budgets/list.html",
        {
            "budgets": budgets
        }
    )


# CREATE
def budget_create(request):

    patients = Patient.objects.filter(
        is_active=True
    )

    treatments = SuggestedTreatment.objects.all()

    if request.method == "POST":

        try:

            Budget.objects.create(

                suggested_treatment_id=request.POST.get(
                    "suggested_treatment_id"
                ),

                patient_id=request.POST.get(
                    "patient_id"
                ),

                issue_date=request.POST.get(
                    "issue_date"
                ),

                gross_total=request.POST.get(
                    "gross_total"
                ),

                discount=request.POST.get(
                    "discount"
                ),

                net_total=request.POST.get(
                    "net_total"
                ),

                budget_status=request.POST.get(
                    "budget_status"
                ),
            )

            messages.success(
                request,
                "Presupuesto registrado"
            )

            return redirect("budget_list")

        except Exception as e:

            messages.error(
                request,
                f"Error: {str(e)}"
            )

            return redirect("budget_create")

    return render(
        request,
        "budgets/form.html",
        {
            "patients": patients,
            "treatments": treatments
        }
    )


# EDIT
def budget_edit(request, id):

    budget = Budget.objects.get(id=id)

    patients = Patient.objects.filter(
        is_active=True
    )

    treatments = SuggestedTreatment.objects.all()

    if request.method == "POST":

        budget.suggested_treatment_id = request.POST.get(
            "suggested_treatment_id"
        )

        budget.patient_id = request.POST.get(
            "patient_id"
        )

        budget.issue_date = request.POST.get(
            "issue_date"
        )

        budget.gross_total = request.POST.get(
            "gross_total"
        )

        budget.discount = request.POST.get(
            "discount"
        )

        budget.net_total = request.POST.get(
            "net_total"
        )

        budget.budget_status = request.POST.get(
            "budget_status"
        )

        budget.save()

        messages.success(
            request,
            "Presupuesto actualizado"
        )

        return redirect("budget_list")

    return render(
        request,
        "budgets/form.html",
        {
            "budget": budget,
            "patients": patients,
            "treatments": treatments
        }
    )