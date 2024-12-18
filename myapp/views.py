from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from jobs.models import Job 
from django.db.models import Q

def index(request):
    # Fetch the search query from the request
    query = request.GET.get('q', '')  # Default to an empty string if 'q' is not in the request

    if query:
        # Filter jobs based on the search query (case-insensitive)
        jobs = Job.objects.filter(
            Q(title__icontains=query) | 
            Q(company__name__icontains=query) |  
            Q(skills_required__icontains=query)  
        )
        no_results = jobs.count() == 0
    else:
        jobs = Job.objects.all()
        no_results = False

    # Pagination: Show 16 jobs per page
    paginator = Paginator(jobs, 16)
    page_number = request.GET.get('page', 1)  
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,  
        'query': query,        
        'no_results': no_results,  
    }
    return render(request, 'home/index.html', context)

def internship(request) :
    internships = Job.objects.filter(job_type__in=["Internship-Private", "Internship-Govt"])

    # Pagination: Show 16 internships per page
    paginator = Paginator(internships, 16)
    page_number = request.GET.get('page', 1)  # Get the current page number from the request
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,  # Contains the paginated internships
    }

    return render(request, 'home/internship_engineering.html', context) 

def job_fulltime(request) :
    jobs = Job.objects.filter(job_type = "Private")
    paginator = Paginator(jobs, 16)
    page_number = request.GET.get('page', 1)  # Get the current page number from the request
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,  # Contains the paginated internships
    }
    
    return render(request, 'home/privatejob.html', context)
    



def aboutus(request) :
    return render(request, 'footer/about.html')


def contactus(request) :
    return render(request, 'footer/contactus.html')