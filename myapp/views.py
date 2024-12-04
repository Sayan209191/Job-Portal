from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from jobs.models import Job 

# Create your views here.

from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import render

from django.db.models import Q

def index(request):
    # Fetch the search query from the request
    query = request.GET.get('q', '')  # Default to an empty string if 'q' is not in the request

    if query:
        # Filter jobs based on the search query (case-insensitive)
        jobs = Job.objects.filter(
            Q(title__icontains=query) | 
            Q(company__name__icontains=query) |  # Adjust for ForeignKey lookup
            Q(skills_required__icontains=query)  # Correct field name for skills
        )
    else:
        # Fetch all jobs if no query is provided
        jobs = Job.objects.all()

    # Pagination: Show 16 jobs per page
    paginator = Paginator(jobs, 16)
    page_number = request.GET.get('page', 1)  # Get the current page number from the request
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,  # Contains the paginated jobs
        'query': query,        # Pass the search query to the template for display
    }
    return render(request, 'home/index.html', context)



def aboutus(request) :
    return render(request, 'footer/about.html')


def contactus(request) :
    return render(request, 'footer/contactus.html')