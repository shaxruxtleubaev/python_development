# Generated by Django 4.1.5 on 2023-01-06 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
