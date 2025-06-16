from django.db import models
from django.conf import settings

from user.models import User
from employer.models import JobPost

class JobApplication(models.Model):
    job_post = models.ForeignKey('employer.JobPost', on_delete=models.CASCADE, related_name='applications')
    job_seeker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applier')
    resume = models.FileField(upload_to='resumes/')
    skill = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    resume_content = models.TextField()
    professional_title = models.CharField(max_length=255)
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('job_post', 'job_seeker')

    def __str__(self):
        return f"{self.job_seeker.username} applied for {self.job_post.title}"

