from django.shortcuts import render
from . models import *
# Create your views here.
def ph(request):
    return render(request,'home.html')
def ph1(request):
    return render(request,'about.html')
def ph2(request):
    return render(request,'contact.html')
def Insertdata (request):
    name = request.POST['name']
    email = request.POST['email']
    contact = request.POST['contact']
    subject = request.POST['subject']

    newuser = contacts.objects.create(
        name=name,email=email ,contact=contact,subject=subject)
    return render(request, 'contact.html')
def ph3(request):
    return render(request,'join team.html')
def ph4(request):
    return render(request,'photo gallery.html')
def ph5(request):
    return render(request,'Events.html')