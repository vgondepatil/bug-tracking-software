# Generated by Django 4.0.5 on 2022-09-13 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='teamleader',
        ),
        migrations.AddField(
            model_name='team',
            name='teamleadermail',
            field=models.EmailField(default='non_assigned', max_length=254),
        ),
    ]