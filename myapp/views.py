from django.shortcuts import render

from .models import Category, ToDo, Appointment


def index(request):
    todo = ToDo.objects.all()
    appointment = Appointment.objects.all()
    context = {'todos': todo, 'appointments': appointment}
    return render(request, 'myapp/index.html', context)
