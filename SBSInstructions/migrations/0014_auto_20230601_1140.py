# Generated by Django 3.2.12 on 2023-06-01 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SBSInstructions', '0013_auto_20230601_0914'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profil',
            options={},
        ),
        migrations.AlterModelManagers(
            name='profil',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='profil',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='profil',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='profil',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='profil',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='profil',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='profil',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='profil',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='profil',
            name='username',
        ),
    ]
