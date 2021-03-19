# Generated by Django 2.2.11 on 2020-03-16 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20200316_2228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='groupId',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='groupName',
            field=models.CharField(default='Unnamed Group', max_length=30),
        ),
        migrations.AlterField(
            model_name='projectgroup',
            name='groupName',
            field=models.CharField(default='Unnamed group', max_length=30, primary_key=True, serialize=False, unique=True),
        ),
    ]