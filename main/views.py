from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "main/acceuil.html")

def moi(request):
    return render(request, "main/moi.html")