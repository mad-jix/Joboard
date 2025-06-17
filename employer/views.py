from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from jobseeker.models import JobApplication

from .models import JobPost
from .forms import JobForm


##Project Requirements : Features - Job posting with title, description, salary, location
@login_required(login_url='login_page') 
def post_job(request):
    if request.user.role != 'employer':
        return redirect('register_employer')

    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            job = form.save(commit=False)
            job.employer = request.user
            job.save()
            messages.success(request, 'Job posted successfully!')
            return redirect('index')
    else:
        form = JobForm()

    return render(request, 'postjob.html', {'form': form})

def applications(request):
    return render(request , 'browse-candidates.html')


@login_required(login_url='login_page') 
def view_applications(request):
    # Get all job posts by this employer
    job_posts = JobPost.objects.filter(employer=request.user)
    
    # Get applications for these job posts, ordered by most recent first
    applications = JobApplication.objects.filter(
        job_post__in=job_posts
    ).select_related('job_seeker', 'job_post').order_by('-applied_at')
    
    context = {
        'applications': applications,
        'title': 'Job Applications'
    }
    return render(request, 'browse-candidates.html', context)
