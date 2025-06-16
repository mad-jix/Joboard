from django.contrib import admin
from .models import JobPost

@admin.register(JobPost)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'employer', 'location', 'job_type', 'work_mode', 'salary', 'deadline', 'posted_at')
    list_filter = ('job_type', 'work_mode', 'location')
    search_fields = ('title', 'description', 'employer__email')