from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        "variable": "variable sent"
    }
    return render(request, "index.html", context)

def about(request):
    return render(request, "sub.html", { "value": "About Us"})

def carrers(request):
    return render(request, "sub.html", { "value": "Carrers"})

def products(request):
    return render(request, "sub.html", {"value": "Products"})