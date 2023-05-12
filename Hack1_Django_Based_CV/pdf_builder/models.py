from django.contrib.auth.models import User
from django.db import models

class PDF(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pdf_file = models.FileField(upload_to='pdfs/')

    # Other fields and methods

    def __str__(self):
        return self.pdf_file.name

# Create your models here.
