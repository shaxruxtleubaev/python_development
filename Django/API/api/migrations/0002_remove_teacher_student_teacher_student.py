# Generated by Django 4.1.6 on 2023-02-02 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='student',
        ),
        migrations.AddField(
            model_name='teacher',
            name='student',
            field=models.ManyToManyField(to='api.students'),
        ),
    ]