from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        "variable": "variable sent"
    }
    return render(request, "index.html", context)
