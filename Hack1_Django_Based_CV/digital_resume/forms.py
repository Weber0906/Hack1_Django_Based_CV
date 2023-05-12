from django import forms
from django.forms import formset_factory, HiddenInput
from .models import TechnicalProject, TechnicalSkill, Experience, Education, Language, Summary


class SummaryForm(forms.ModelForm):
    class Meta:
        model = Summary
        fields = ['user_profile', 'summary_text']
        widgets = {
            'user_profile': HiddenInput(),
        }


class TechnicalSkillForm(forms.ModelForm):
    class Meta:
        model = TechnicalSkill
        fields = ['user_profile', 'skill_name']
        widgets = {
            'user_profile': HiddenInput(),
        }


class TechnicalProjectForm(forms.ModelForm):
    class Meta:
        model = TechnicalProject
        fields = ['user_profile', 'project_name', 'github_url', 'demo_url', 'project_description']
        widgets = {
            'user_profile': HiddenInput(),
        }


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['user_profile', 'job_title', 'company_name', 'start_date', 'end_date', 'experience_description']
        widgets = {
            'user_profile': HiddenInput(),
        }


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['user_profile', 'program_name', 'institution_name', 'start_date', 'end_date']
        widgets = {
            'user_profile': HiddenInput(),
        }


class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['user_profile', 'language_name', 'proficiency_level']
        widgets = {
            'user_profile': HiddenInput(),
        }



