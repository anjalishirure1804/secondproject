from django.shortcuts import render
from .models import *
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    context = {'success': False}
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        contact = request.POST['contact']
        dob = request.POST['dob']
        con = Contact(username=username, email=email, contact=contact,dob=dob)
        con.save()

        context = {'success': True}
        love(username, email)

    return render(request, 'app/index.html', context)


def love(user, email):
    print(user, email)
    send_mail(
        'congratulations!!!! your form has been submitted successfully',

        user,
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )
    


def show(request):
    allTask = Contact.objects.all()

    context = {
        'tasks': allTask
    }
    print(allTask)
    return render(request, 'app/show.html', context)