# Generated by Django 4.1.4 on 2022-12-13 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=75, null=True, verbose_name='Заголовок')),
                ('price', models.FloatField(default=0, verbose_name='Цена')),
                ('num_bedrooms', models.IntegerField(verbose_name='Комната')),
                ('num_bathrooms', models.IntegerField(verbose_name='Ванная')),
                ('square_footage', models.IntegerField(verbose_name='Площадь')),
                ('adress', models.CharField(max_length=100, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Список комнат',
                'verbose_name_plural': 'Списки',
                'ordering': ('-price',),
            },
        ),
    ]
