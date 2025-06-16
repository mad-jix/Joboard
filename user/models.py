from django.db import models
from django.contrib.auth.models import AbstractUser

# ---------------------------
# Custom User Model
# ---------------------------
class User(AbstractUser):
    ROLE_CHOICES = (
        ('job_seeker', 'Job Seeker'),
        ('employer', 'Employer'),
        ('admin', 'Admin'),
    )

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    companyname = models.CharField(max_length=255, blank=True, null=True)

    # ✅ Use email as the unique login field
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # Only needed for job_seekers

    def __str__(self):
        return f"{self.email} ({self.role})"