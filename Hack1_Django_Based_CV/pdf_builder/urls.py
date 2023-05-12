from django.urls import path
from .views import generate_pdf, preview_information

app_name = 'pdf_builder'

urlpatterns = [
    path('generate-pdf/', generate_pdf, name='generate-pdf'),
    path('preview/', preview_information, name='preview')
]