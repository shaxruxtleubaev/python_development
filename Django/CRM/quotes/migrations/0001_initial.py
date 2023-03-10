# Generated by Django 4.1.5 on 2023-01-12 10:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('position', models.CharField(blank=True, max_length=60, null=True)),
                ('company', models.CharField(blank=True, max_length=60, null=True)),
                ('address', models.CharField(blank=True, max_length=150, null=True)),
                ('phone', models.CharField(blank=True, max_length=60, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('web', models.URLField(blank=True)),
                ('description', models.TextField()),
                ('sitestatus', models.CharField(choices=[('NEW', 'New site'), ('EX', 'Existing site')], max_length=60)),
                ('priority', models.CharField(choices=[('U', 'Urgent - 1 week or less'), ('N', 'Normal - 2 to 4 weeks'), ('L', 'Low - Still researching')], max_length=60)),
                ('jobfile', models.FileField(blank=True, upload_to='uploads/')),
                ('submitted', models.DateField(auto_now_add=True)),
                ('quotedate', models.DateField(auto_now_add=True)),
                ('quoteprice', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
