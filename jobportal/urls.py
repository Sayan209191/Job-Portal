from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # For Google sign-in and other allauth functionalities
    path('auth/', include('accounts.urls')),      # For your custom sign-in, sign-up, logout views
    path('', include('myapp.urls')), 

    # path('job/', include('jobs.url')) 
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)