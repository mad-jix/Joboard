from django.urls import path
from . import views

urlpatterns = [
    path('job-detail/<int:job_id>/', views.job_detail, name='job_detail'),
    path('browse-job/', views.browse_jobs, name='browse-job'),
    path('applyjob/<int:job_id>/', views.apply_to_job, name='apply_job'),
]


