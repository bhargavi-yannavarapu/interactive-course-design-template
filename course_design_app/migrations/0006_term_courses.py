# Generated by Django 4.1.7 on 2023-10-17 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_design_app', '0005_remove_term_courses_alter_term_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='term',
            name='courses',
            field=models.ManyToManyField(related_name='terms', to='course_design_app.course'),
        ),
    ]
