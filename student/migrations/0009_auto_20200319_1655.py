# Generated by Django 2.2.11 on 2020-03-19 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_auto_20200316_2304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='cgpa',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='image',
        ),
    ]