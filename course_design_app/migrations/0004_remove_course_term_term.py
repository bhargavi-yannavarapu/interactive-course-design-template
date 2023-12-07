# Generated by Django 4.1.7 on 2023-10-17 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_design_app', '0003_course_term_alter_course_name_delete_term'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='term',
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('courses', models.ManyToManyField(related_name='terms', to='course_design_app.course')),
            ],
        ),
    ]