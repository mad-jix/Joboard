from django.urls import path
from .import views

urlpatterns = [
    
    path('post-job/', views.post_job, name="post-job"),
    path('applications/',  views.view_applications, name='view_applications'),
]