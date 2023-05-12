from typing import Any, Dict
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.forms import formset_factory
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.urls import reverse_lazy
from .models import *
from django.views.generic import TemplateView
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import UserProfile

# Create your views here.
class BaseCreateView(FormView):
    formset_class = None  # Override this in child views
    template_name = None  # Override this in child views
    success_url = None  # Override this in child views

    def get_form(self, form_class=None):
        formset = self.formset_class(**self.get_form_kwargs())
        for form in formset:
            form.fields['user_profile'].initial = self.request.user.profile
        return formset

    def form_valid(self, form):
        for form_instance in form:
            if form_instance.is_valid():
                form_instance.save()
        return super().form_valid(form)

class GreetingsView(TemplateView):
    def get(self, request):
        return render(request, 'digital_resume/greetings.html')

class PersonalInfoCreateView(LoginRequiredMixin, CreateView):
    model = PersonalInfo
    fields = ['first_name', 'last_name', 'job_title', 'city', 'phone_number', 'email', 'github_url', 'linkedin_url', 'portfolio_url']
    template_name = 'digital_resume/personal_info_form.html'
    success_url = reverse_lazy('digital_resume:summary-create')

    def form_valid(self, form):

        user_profile = UserProfile.objects.get(user=self.request.user)

        form.instance.user_profile = user_profile
        return super().form_valid(form)

class SummaryCreateView(FormView):
    form_class = SummaryForm
    template_name = 'digital_resume/summary_form.html'
    success_url = reverse_lazy('digital_resume:technical-skill-create')
    

    def get_form(self, form_class=None) -> Dict[str, Any]:
        form = super().get_form(form_class)
        user_profile = self.request.user.profile
        form.fields['user_profile'].initial = user_profile
        return form
    
    def form_valid(self, form) -> HttpResponse:
        form.save()
        return super().form_valid(form)


class TechnicalSkillCreateView(BaseCreateView):
    formset_class = formset_factory(TechnicalSkillForm, extra=2)
    template_name = 'digital_resume/technical_skill_form.html'
    success_url = reverse_lazy('digital_resume:technical-project-create')
    

class TechnicalProjectCreateView(BaseCreateView):
    formset_class = formset_factory(TechnicalProjectForm, extra=2)
    template_name = 'digital_resume/technical_project_form.html'
    success_url = reverse_lazy('digital_resume:experience-create')


class ExperienceCreateView(BaseCreateView):
    formset_class = formset_factory(ExperienceForm, extra=2)
    template_name = 'digital_resume/experience_form.html'
    success_url = reverse_lazy('digital_resume:education-create')


class EducationCreateView(BaseCreateView):
    formset_class = formset_factory(EducationForm, extra=2)
    template_name = 'digital_resume/education_form.html'
    success_url = reverse_lazy('digital_resume:language-create')


class LanguageCreateView(BaseCreateView):
    formset_class = formset_factory(LanguageForm, extra=3)
    template_name = 'digital_resume/language_form.html'
    success_url = reverse_lazy('pdf_builder:preview')
