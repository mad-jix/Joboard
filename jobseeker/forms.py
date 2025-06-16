import os
from django import forms
from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['professional_title', 'location', 'resume', 'resume_content', 'skill']
        widgets = {
            'professional_title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Senior Software Engineer'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. New York, USA'
            }),
            'resume_content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Paste your resume content here...'
            }),
            'skill': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Python, Django, JavaScript'
            }),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['resume'].widget.attrs.update({
            'class': 'form-control-file',
            'accept': '.pdf,.doc,.docx'
        })
        # Set required=False for resume if you want it to be optional
        # self.fields['resume'].required = False

    def clean(self):
        cleaned_data = super().clean()
        if self.user and self.user.role != 'job_seeker':
            raise forms.ValidationError("Only job seekers can submit job applications.")
        
        resume = cleaned_data.get('resume')
        if resume:  # Only validate if resume was uploaded
            valid_extensions = ['.pdf', '.doc', '.docx']
            extension = os.path.splitext(resume.name)[1].lower()
            if extension not in valid_extensions:
                raise forms.ValidationError("Unsupported file format. Please upload PDF, DOC, or DOCX.")
            
            # Validate file size (5MB limit)
            if resume.size > 5 * 1024 * 1024:
                raise forms.ValidationError("File size exceeds 5MB limit.")
        
        return cleaned_data