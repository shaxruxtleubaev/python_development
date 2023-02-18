# Generated by Django 3.2 on 2022-12-02 17:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name_plural': 'Author'},
        ),
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name_plural': 'Blog'},
        ),
        migrations.AlterModelOptions(
            name='entry',
            options={'verbose_name_plural': 'Entry'},
        ),
        migrations.CreateModel(
            name='Quest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
