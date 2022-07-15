from concurrent.futures.process import _python_exit
import email
from statistics import variance
from tkinter import Variable
from urllib import request
from django.shortcuts import render
from django.shortcuts import HttpResponse
from datetime import datetime
from home.models import Contact

# Create your views here.
def index(request):
    
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, "services.html")



def contact(request):
    context = {
        "variable":""
    }
    
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        code = request.POST.get("code")
        desc = request.POST.get("desc")
        contact = Contact(name=name, email=email, phone=phone, code=code, desc=desc, date=datetime.today())
        contact.save()

    
    return render(request, "contact.html", context)