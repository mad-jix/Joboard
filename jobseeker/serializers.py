from rest_framework import serializers
from .models import JobPost

class JobPostSerializer(serializers.ModelSerializer):
    employer_name = serializers.CharField(source='employer.companyname', read_only=True)
    job_type_display = serializers.CharField(source='get_job_type_display', read_only=True)
    work_mode_display = serializers.CharField(source='get_work_mode_display', read_only=True)

    class Meta:
        model = JobPost
        fields = [
            'id',
            'title',
            'description',
            'location',
            'salary',
            'experience',
            'deadline',
            'job_type',
            'work_mode',
            'job_type_display',
            'work_mode_display',
            'employer_name',
        ]
