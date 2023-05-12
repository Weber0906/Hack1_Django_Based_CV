from django.db import models
from accounts.models import UserProfile


class PersonalInfo(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='personal_info')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    github_url = models.URLField()
    linkedin_url = models.URLField()
    portfolio_url = models.URLField()
    # other fields as per your requirements

class Summary(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    summary_text = models.TextField()

class TechnicalSkill(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='tech_skills')
    skill_name = models.CharField(max_length=255)

    def __str__(self):
        return self.skill_name

class TechnicalProject(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='tech_projects')
    project_name = models.CharField(max_length=255)
    github_url = models.URLField()
    demo_url = models.URLField()
    project_description = models.TextField()

    def __str__(self):
        return self.project_name

class Experience(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='experience')
    job_title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    experience_description = models.TextField()

    def __str__(self):
        return self.job_title

class Education(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='education')
    program_name = models.CharField(max_length=255)
    institution_name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.program_name

class Language(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='languages')
    language_name = models.CharField(max_length=255)
    proficiency_level = models.CharField(max_length=255)

    def __str__(self):
        return self.language_name