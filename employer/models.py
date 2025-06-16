from django.db import models

from user.models import User


class JobPost(models.Model):
    JOB_TYPE_CHOICES =  [      
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('freelance', 'Freelance'),
        ('internship', 'Internship'),
    ]

    WORK_MODE_CHOICES = [
        ('remote', 'Work From Home'),
        ('office', 'In Office'),
        ('hybrid', 'Hybrid'),
    ]

    employer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='company')
    title = models.CharField (max_length=255)
    description = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    experience = models.CharField(max_length=100)
    deadline = models.DateField()
    education = models.CharField(max_length=255)
    how_to_apply = models.TextField()
    requirements = models.TextField()
    company_logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)
    work_mode = models.CharField(max_length=20, choices=WORK_MODE_CHOICES)
    posted_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title