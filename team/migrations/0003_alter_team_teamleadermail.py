# Generated by Django 4.0.5 on 2022-09-13 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_remove_team_teamleader_team_teamleadermail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='teamleadermail',
            field=models.EmailField(default='non_assigned', max_length=254, null=True),
        ),
    ]
