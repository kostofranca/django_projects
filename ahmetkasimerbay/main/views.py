from django.shortcuts import render

# Create your views here.

content = {
    "name": "Ahmet Kasım Erbay",
}

def index(request):
    return render(request, "main/index.html", content)

