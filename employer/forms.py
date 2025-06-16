from django import forms
from .models import JobPost

class JobForm(forms.ModelForm):
    deadline = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d']  # Add allowed formats
    )

    class Meta:
        model = JobPost
        fields = [
            'title', 'description', 'salary', 'location', 'experience',
            'deadline', 'education', 'how_to_apply', 'requirements',
            'company_logo', 'job_type', 'work_mode'
        ]