# Generated by Django 4.1.7 on 2023-03-16 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calories', '0007_alter_postexercise_calorie_burned'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postexercise',
            name='duration',
            field=models.FloatField(default=0),
        ),
    ]