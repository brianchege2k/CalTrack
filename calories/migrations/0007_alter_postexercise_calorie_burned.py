# Generated by Django 4.1.7 on 2023-03-16 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calories', '0006_rename_calorie_lost_postexercise_calorie_burned_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postexercise',
            name='calorie_burned',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
