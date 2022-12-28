# Generated by Django 4.1.4 on 2022-12-15 09:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Имя')),
                ('body', models.TextField(blank=True, null=True, verbose_name='Тело')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('stock', models.BooleanField(verbose_name='Сток')),
                ('color', models.CharField(blank=True, max_length=200, null=True, verbose_name='Цвет')),
                ('author', models.CharField(blank=True, max_length=200, null=True, verbose_name='Автор')),
            ],
        ),
    ]