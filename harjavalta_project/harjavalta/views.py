from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse

def index(request):
    return render(request, 'index.html')

def koti(request):
    return redirect('index')  # Redirect to the landing page

def työpaikat(request):
    return render(request, 'työpaikat.html')

def yrityksille(request):
    return render(request, 'yrityksille.html')

def työntekijöille(request):
    return render(request, 'työntekijöille.html')

def info(request):
    return render(request, 'info.html')