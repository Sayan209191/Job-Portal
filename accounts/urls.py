from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.handlelogin, name='login'),
    path('logout/', views.handlelogout, name='logout'),
    path('request-reset-email/',views.RequestResetEmailView.as_view(),name='request-reset-email'),
    path('set-new-password/<uidb64>/<token>',views.SetNewPasswordView.as_view(),name='set-new-password'),
    path('profile/', views.profile_view, name='profile_view'),      # View Profile
    path('profile/edit/', views.profile_edit, name='profile_edit'), # Edit Profile
    path('add-work/', views.add_work_experience, name='add_work_experience'),
    path('edit-work/<int:pk>/', views.edit_work_experience, name='edit_work_experience'),
    path('add-education/', views.add_education, name='add_education'),
    path('edit-education/<int:pk>/', views.edit_education, name='edit_education'),
]

