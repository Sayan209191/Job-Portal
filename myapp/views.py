from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
from jobs.models import Company, Job 
from django.db.models import Q
from django.core.mail import send_mail
from .models import ContactMessage
from django.conf import settings

def index(request):
    # Fetch the search query from the request
    query = request.GET.get('q', '').strip()   

    if query:
        # Filter jobs based on the search query (case-insensitive)
        jobs = Job.objects.filter(
            Q(title__icontains=query) | 
            Q(company__name__icontains=query) |  
            Q(skills_required__icontains=query)|
            Q(job_type__icontains=query)|
            Q(location__icontains=query)
            # Q(company__icontains=query) 
        ).order_by('-date_posted') 
        no_results = jobs.count() == 0
    else:
        jobs = Job.objects.all().order_by('-date_posted')
        no_results = False

    # Pagination: Show 40 jobs per page         
    paginator = Paginator(jobs,16)
    page_number = request.GET.get('page', 1)  
    page_obj = paginator.get_page(page_number)

    
    total_pages = paginator.num_pages
    current_page = page_obj.number
    start_page = (current_page - 1) // 10 * 10 + 1
    end_page = min(start_page + 9, total_pages)

    page_range = range(start_page, end_page + 1)

    context = {
        'page_obj': page_obj,  
        'query': query,        
        'no_results': no_results,  
        'page_range': page_range,  
    }
    return render(request, 'home/index.html', context)

def internship(request) :
    internships = Job.objects.filter(job_type__in=["Internship-Private", "Internship-Govt"]).order_by('-date_posted') 

    # Pagination: Show 16 internships per page
    paginator = Paginator(internships, 16)
    page_number = request.GET.get('page', 1)  # Get the current page number from the request
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,  # Contains the paginated internships
    }

    return render(request, 'home/internship_engineering.html', context) 

def job_fulltime(request) :
    jobs = Job.objects.filter(job_type="Private", date_posted__isnull=False).order_by('-date_posted')

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
    if request.method == "POST":
        # Extract data from the form
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save the data to the database
        ContactMessage.objects.create(name=name, email=email, message=message)

        # Send an auto-generated email
        send_mail(
            subject="Thank You for Contacting Us!",
            message=(
                "Hello,\n\n"
                f"Dear {name},\n"
                "Thank you for reaching out to us. We have received your message and will get back to you soon.\n\n"
                "Best regards,\nMake Your Career Team"
            ),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
            fail_silently=False,
        )

        # Redirect to a thank-you page
        # --- make the than you page
        return redirect('/')

    # Render the contact form page
    return render(request, 'footer/contactus.html')

def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, 'home/jobdescription.html', {'job': job})


def company_overview(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    jobs = Job.objects.filter(company=company)  # Get all jobs by this company
    return render(request, 'home/companydescription.html', {'company': company, 'jobs': jobs})


def remote_jobs(request):
    jobs = Job.objects.filter(location__icontains="Remote").order_by('-date_posted') 
    paginator = Paginator(jobs, 16)
    page_number = request.GET.get('page', 1)  # Get the current page number from the request
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,  # Contains the paginated internships
    }
    
    return render(request, 'home/remotejob.html', context)

def search_suggestions(request):
    query = request.GET.get('q', '').strip()
    suggestions = []

    if query:
        jobs = Job.objects.filter(
            Q(title__icontains=query) | 
            Q(company__name__icontains=query) |
            Q(skills_required__icontains=query)
        ).distinct()[:10]  # Limit results to 10 suggestions

        suggestions = list(jobs.values_list('title', flat=True))  # Get only job titles

    return JsonResponse({'suggestions': suggestions})