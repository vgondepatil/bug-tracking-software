# Generated by Django 4.0.5 on 2022-09-30 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0008_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='system',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system_name', models.CharField(max_length=30)),
                ('system_mail', models.EmailField(max_length=254)),
                ('system_password', models.CharField(max_length=30)),
            ],
        ),
    ]
