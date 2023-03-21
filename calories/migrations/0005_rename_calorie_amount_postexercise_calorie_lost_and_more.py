# Generated by Django 4.1.7 on 2023-03-15 11:12

import calories.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calories', '0004_exercise_person_of'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postexercise',
            old_name='calorie_amount',
            new_name='calorie_lost',
        ),
        migrations.AddField(
            model_name='profile',
            name='duration',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name=calories.models.Exercise),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='food',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='postexercise',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='postfood',
            name='calorie_amount',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='postfood',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='total_calorie',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]