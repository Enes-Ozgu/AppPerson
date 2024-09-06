from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from . import views
from .models import Person
from django.contrib.auth.decorators import login_required
from .forms import PersonForm
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
@login_required(login_url = "user:login")
def dashboard(request):
    persons = Person.objects.filter(first_name = request.user.username)
    context = {
        "Persons":Person

    }
    return render(request,"dashboard.html",context)
@login_required(login_url = "user:login")
def addcontact(request):
    form = PersonForm(request.POST or None)

    if form.is_valid():
        Person = form.save(commit=False)

        Person.first_name = request.user
        Person.save()
        messages.success(request,"Contact saved.")
        return redirect("contact:dashboard")
        
    return render(request,"addcontact.html",{"form":form})
@login_required(login_url = "user:login")
def updatecontact(request,id):

    Person = get_object_or_404(Person,id = id)

    form = PersonForm(request.POST or None,instance = Person)
    if form.is_valid():
        Person = form.save(commit=False)
        Person.first_name = request.user
        Person.save()
        messages.success(request,"Contact updated.")
        return redirect("contact:dashboard") 

    return render(request,"update.html",{"form":form})
@login_required(login_url = "user:login")
def deletecontact(request,id):
    Person = get_object_or_404(Person,id = id)

    Person.delete()
    messages.success(request,"Contact deleted")

    return render("contact:dashboard")
