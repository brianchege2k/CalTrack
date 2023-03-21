# Generated by Django 4.1.7 on 2023-03-16 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calories', '0008_alter_postexercise_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='all_exercises_selected_today',
            field=models.ManyToManyField(related_name='exercises', through='calories.PostExercise', to='calories.exercise'),
        ),
    ]