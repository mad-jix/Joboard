from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from .forms import JobSeekerRegisterForm, EmployerRegisterForm, CustomLoginForm

from employer.models import JobPost

def register_job_seeker(request):
    if request.method == 'POST':
        form = JobSeekerRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Job Seeker registered successfully.")
            return redirect('login_page')
    else:
        form = JobSeekerRegisterForm()
    return render(request, 'jobseeker_reg.html', {'form': form})

def register_employer(request):
    if request.method == 'POST':
        form = EmployerRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Employer registered successfully.")
            return redirect('login_page')
    else:
        form = EmployerRegisterForm()
    return render(request, 'employer_reg.html', {'form': form})

@require_http_methods(["GET", "POST"])
def login_page(request):
    # If user is already authenticated, redirect them appropriately
    if request.user.is_authenticated:
        return redirect_based_on_role(request.user)

    if request.method == 'POST':
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect_based_on_role(user)
        
        # Form is invalid - errors will be displayed in template
        messages.error(request, "Invalid credentials. Please try again.")
    else:
        form = CustomLoginForm()
    
    return render(request, 'login.html', {
        'form': form,
        'title': 'Login'
    })

def redirect_based_on_role(user):
    """Helper function to handle redirects based on user role"""
    if user.is_superuser:
        return redirect('/admin/')
    
    # Add any additional role checks here
    return redirect('index') 

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login_page') 

def index(request):
    latest_jobs = JobPost.objects.order_by('-posted_at')[:20]
    return render(request, 'index.html', {'latest_jobs': latest_jobs})


def about(request):
    return render(request , 'about-us.html')





