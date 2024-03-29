# Generated by Django 4.2.7 on 2023-11-17 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filter_app', '0004_student_gpa_student_receives_scholarship'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='kurs',
            new_name='courses',
        ),
        migrations.AlterField(
            model_name='car',
            name='color',
            field=models.CharField(blank=True, choices=[('white', 'white'), ('black', 'black'), ('red', 'red'), ('blue', 'blue'), ('violet', 'violet'), ('pink', 'pink'), ('yellow', 'yellow')], max_length=20, verbose_name='цвет'),
        ),
        migrations.AlterField(
            model_name='student',
            name='group',
            field=models.CharField(max_length=6),
        ),
    ]
