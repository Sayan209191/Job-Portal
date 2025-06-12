from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('contact-us', views.contactus, name='contact-us'),
    path('internship', views.internship, name='internship'),
    path('privatejob', views.job_fulltime, name='privatejob'),
    path('job/<int:job_id>/', views.job_detail, name='job_detail'),
    path('job/<int:job_id>/toggle-save/', views.save_or_unsave_job, name='save_or_unsave_job'),
    path('company/<int:company_id>/', views.company_overview, name='company_overview'),
    path('RemoteJob', views.remote_jobs, name='Remotejob'),
    path('search-suggestions/', views.search_suggestions, name='search_suggestions'),
    path('search/', views.search_results, name='search_results'),
    path("track-apply/<int:job_id>/", views.track_application, name="track_application"),
]
