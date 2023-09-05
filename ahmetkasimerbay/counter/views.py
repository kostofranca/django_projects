from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {
        "counter": "counter"
    }

    return render(request, "counter/index.html", context)