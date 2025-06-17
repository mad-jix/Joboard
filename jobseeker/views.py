from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import JobApplication
from .forms import JobApplicationForm
from employer.models import JobPost



def job_detail(request, job_id):
    job = get_object_or_404(JobPost, id=job_id)
    return render(request, 'jobdetail.html', {'job': job})

#Project Requirements : Features - Job search with filters (location, category, company)
def browse_jobs(request):
    jobs = JobPost.objects.all().order_by('-posted_at')

    # Check for filters
    location = request.GET.get('location')
    job_type = request.GET.get('category')
    company = request.GET.get('company')

    # Apply filters only if values exist
    if location:
        jobs = jobs.filter(location__icontains=location)

    if job_type:
        jobs = jobs.filter(job_type=job_type)

    if company:
        jobs = jobs.filter(employer__username__icontains=company)

    return render(request, 'browsejob.html', {'jobs': jobs})



#Project Requirements : Features - Users can apply for jobs
@login_required(login_url='login_page') 
def apply_to_job(request, job_id):
    job_post = get_object_or_404(JobPost, id=job_id)

    # Check if user is a job seeker
    if request.user.role != 'job_seeker':
        messages.error(request, "Only job seekers can apply for jobs.")
        return redirect('job_detail', job_id=job_id)

    # Check if already applied
    if JobApplication.objects.filter(job_post=job_post, job_seeker=request.user).exists():
        messages.warning(request, "You've already applied for this position.")
        return redirect('job_detail', job_id=job_id)

    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            application = form.save(commit=False)
            application.job_post = job_post
            application.job_seeker = request.user
            application.save()
            messages.success(request, "Your application was submitted successfully!")
            return redirect('job_detail', job_id=job_id)
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = JobApplicationForm(user=request.user)

    context = {
        'form': form,
        'job': job_post,
        'title': f'Apply for {job_post.title}'
    }
    return render(request, 'submit-resume.html', context)
