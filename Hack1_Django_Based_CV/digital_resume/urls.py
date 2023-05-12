from django.urls import path
from . import views

app_name = 'digital_resume'

urlpatterns = [
    path('', views.GreetingsView.as_view(), name='greetings'),
    path('personal-info/create', views.PersonalInfoCreateView.as_view(), name='personal-info-create'),
    path('summary/create/', views.SummaryCreateView.as_view(), name='summary-create'),
    path('technical-skill/create/', views.TechnicalSkillCreateView.as_view(), name='technical-skill-create'),
    path('technical-project/create/', views.TechnicalProjectCreateView.as_view(), name='technical-project-create'),
    path('experience/create/', views.ExperienceCreateView.as_view(), name='experience-create'),
    path('education/create/', views.EducationCreateView.as_view(), name='education-create'),
    path('language/create/', views.LanguageCreateView.as_view(), name='language-create'),
]