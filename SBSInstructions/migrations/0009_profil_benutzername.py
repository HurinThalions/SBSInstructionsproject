# Generated by Django 3.2.12 on 2023-06-01 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SBSInstructions', '0008_auto_20230531_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='benutzername',
            field=models.CharField(default=1, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
