from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # info = models.OneToOneField('PersonalInfo', on_delete=models.CASCADE, null=True, blank=True)
    # summary_text = models.OneToOneField('Summary', on_delete=models.CASCADE, null=True, blank=True)
    # technical_skills = models.ManyToManyField('TechnicalSkill')
    # technical_projects = models.ManyToManyField('TechnicalProject')
    # experiences = models.ManyToManyField('Experience')
    # educations = models.ManyToManyField('Education')
    # languages = models.ManyToManyField('Language')


    def __str__(self):
        return f"{self.user.username}"
