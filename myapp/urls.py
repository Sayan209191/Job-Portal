from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('contact-us', views.contactus, name='contact-us'),
    path('internship', views.internship, name='internship'),
    path('privatejob', views.job_fulltime, name='job_fulltime'),
    path('job/<int:job_id>/', views.job_detail, name='job_detail'),
    path('company/<int:company_id>/', views.company_overview, name='company_overview'),
]
