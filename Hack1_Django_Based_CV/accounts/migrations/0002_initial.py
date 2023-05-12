# Generated by Django 4.2 on 2023-05-08 06:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('digital_resume', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='educations',
            field=models.ManyToManyField(to='digital_resume.education'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='experiences',
            field=models.ManyToManyField(to='digital_resume.experience'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='info',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='digital_resume.personalinfo'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='languages',
            field=models.ManyToManyField(to='digital_resume.language'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='summary_text',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='digital_resume.summary'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='technical_projects',
            field=models.ManyToManyField(to='digital_resume.technicalproject'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='technical_skills',
            field=models.ManyToManyField(to='digital_resume.technicalskill'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]