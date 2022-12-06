# Generated by Django 3.2 on 2022-12-06 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('author', models.CharField(blank=True, max_length=40, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
