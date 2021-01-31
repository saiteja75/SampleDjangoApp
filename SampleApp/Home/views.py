from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "variable": "variable sent"
    }
    return render(request, "index.html", context)

def about(request):
    return render(request, "sub.html", { "value": "About Us"})

def contact(request):
    if request.method == "POST":
        name = request.POST.get("txtName")
        email = request.POST.get("txtEmail")
        phno = request.POST.get("txtPhone")
        msg = request.POST.get("txtMsg")
        contact = Contact(name=name,email=email,phno=phno,msg=msg,datetime=datetime.now())
        contact.save()
        messages.success(request, 'Your Message Sent!.')
    return render(request, "contact.html")

def products(request):
    return render(request, "sub.html", {"value": "Products"})