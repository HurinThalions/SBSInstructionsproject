# Generated by Django 3.2.12 on 2023-06-01 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('SBSInstructions', '0020_profil_benutzername'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='email',
            field=models.EmailField(default=2, max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profil',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='profil_set', to='auth.Group'),
        ),
        migrations.AddField(
            model_name='profil',
            name='password',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profil',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_name='profil_set', to='auth.Permission'),
        ),
    ]
