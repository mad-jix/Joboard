from django.contrib import admin
from .forms import JobApplication

# Register your models here.
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('job_seeker', 'job_post', 'professional_title', 'applied_at')
    list_filter = ('applied_at', 'job_post')
    search_fields = ('job_seeker__username', 'job_seeker__email', 'job_post__title')
    readonly_fields = ('applied_at',)
    fieldsets = (
        (None, {
            'fields': ('job_seeker', 'job_post', 'applied_at')
        }),
        ('Application Details', {
            'fields': ('professional_title', 'location', 'skill', 'resume_content')
        }),
        ('Resume', {
            'fields': ('resume',)
        }),
    )

admin.site.register(JobApplication, JobApplicationAdmin)