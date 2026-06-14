from django.shortcuts import render, redirect

from clinic.models.payment import Payment
from clinic.models.budget import Budget
from clinic.models.appointment import Appointment

from django.contrib import messages


# LIST
def payment_list(request):

    payments = Payment.objects.all()

    return render(
        request,
        "payments/list.html",
        {
            "payments": payments
        }
    )


# CREATE
def payment_create(request):

    budgets = Budget.objects.all()

    appointments = Appointment.objects.all()

    if request.method == "POST":

        try:

            Payment.objects.create(

                budget_id=request.POST.get("budget_id") or None,

                appointment_id=request.POST.get(
                    "appointment_id"
                ) or None,

                amount=request.POST.get("amount"),

                payment_method=request.POST.get(
                    "payment_method"
                ),

                reference_number=request.POST.get(
                    "reference_number"
                ),
            )

            messages.success(
                request,
                "Pago registrado correctamente"
            )

            return redirect("payment_list")

        except Exception as e:

            messages.error(
                request,
                f"Error: {str(e)}"
            )

            return redirect("payment_create")

    return render(
        request,
        "payments/form.html",
        {
            "budgets": budgets,
            "appointments": appointments
        }
    )


# EDIT
def payment_edit(request, id):

    payment = Payment.objects.get(id=id)

    budgets = Budget.objects.all()

    appointments = Appointment.objects.all()

    if request.method == "POST":

        payment.budget_id = request.POST.get(
            "budget_id"
        ) or None

        payment.appointment_id = request.POST.get(
            "appointment_id"
        ) or None

        payment.amount = request.POST.get(
            "amount"
        )

        payment.payment_method = request.POST.get(
            "payment_method"
        )

        payment.reference_number = request.POST.get(
            "reference_number"
        )

        payment.save()

        messages.success(
            request,
            "Pago actualizado"
        )

        return redirect("payment_list")

    return render(
        request,
        "payments/form.html",
        {
            "payment": payment,
            "budgets": budgets,
            "appointments": appointments
        }
    )