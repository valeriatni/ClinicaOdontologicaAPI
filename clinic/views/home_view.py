from django.shortcuts import render

def home(request):

    context = {
        'title': 'Dental Clinic System',
        'message': 'Welcome to the management system'
    }

    return render(request, 'home.html', context)