from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about_us'),
    path('register/jobseeker/', views.register_job_seeker, name='register_jobseeker'),
    path('register/employer/', views.register_employer, name='register_employer'),
    path('login/', views.login_page, name='login_page'),
    path('logout/', views.logout_view, name='logout'),
]