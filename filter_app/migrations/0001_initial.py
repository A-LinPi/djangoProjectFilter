# Generated by Django 4.2.5 on 2023-10-28 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=20, verbose_name='марка')),
                ('cost', models.IntegerField(verbose_name='цена')),
                ('year', models.IntegerField(verbose_name='год выпуска')),
                ('color', models.CharField(choices=[('white', 'white'), ('black', 'black'), ('red', 'red'), ('blue', 'blue')], max_length=20, verbose_name='цвет')),
            ],
        ),
    ]
