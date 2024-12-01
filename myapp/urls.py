from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('contact-us', views.contactus, name='contact-us'),
]
