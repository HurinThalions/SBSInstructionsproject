# Generated by Django 3.2.12 on 2023-05-31 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SBSInstructions', '0007_rename_passwort_profil_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anleitung',
            name='ersteller',
        ),
        migrations.RemoveField(
            model_name='profil',
            name='ersteller',
        ),
    ]
