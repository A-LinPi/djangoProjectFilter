# Generated by Django 4.2.7 on 2023-11-11 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filter_app', '0002_company_alter_car_brand_alter_car_color_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('cost', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('group', models.CharField(max_length=4)),
                ('kurs', models.ManyToManyField(to='filter_app.course')),
            ],
        ),
    ]
