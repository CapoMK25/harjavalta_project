from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from .models import Jobs
from django.template.loader import get_template
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def koti(request):
    return redirect('index')  # Redirect to the landing page

def jobs(request):
    job_listings = Jobs.objects.all()
    return render(request, 'jobs.html', {'job_listings': job_listings})


def yrityksille(request):
    return render(request, 'yrityksille.html')

def työntekijöille(request):
    return render(request, 'työntekijöille.html')

def info(request):
    return render(request, 'info.html')