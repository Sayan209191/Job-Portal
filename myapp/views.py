from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from jobs.models import Job 

# Create your views here.

def index(request) :
    # Fetch all jobs from the database
    jobs = Job.objects.all()

    # Pagination: Show 12 jobs per page
    paginator = Paginator(jobs, 16)
    page_number = request.GET.get('page', 1)  # Get the current page number from the request
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,  # Contains the paginated jobs
    }
    return render(request, 'home/index.html', context)

def aboutus(request) :
    return render(request, 'footer/about.html')


def contactus(request) :
    return render(request, 'footer/contactus.html')