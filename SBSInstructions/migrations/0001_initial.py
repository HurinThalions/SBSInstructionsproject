# Generated by Django 3.2.12 on 2023-04-18 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anleitung',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anleittitel', models.CharField(max_length=100)),
                ('ersteller', models.CharField(max_length=100)),
                ('kategorie', models.CharField(max_length=100)),
                ('dauer', models.TimeField(auto_now_add=True)),
                ('datum', models.DateField(verbose_name='datum_erstellt')),
            ],
        ),
        migrations.CreateModel(
            name='Anleitungsschritt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schrittbenennung', models.CharField(max_length=50)),
                ('beschreibung', models.CharField(max_length=500)),
                ('anleitung', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SBSInstructions.anleitung')),
            ],
        ),
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('passwort', models.CharField(max_length=100)),
                ('ersteller', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Komponente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kompbeschreibung', models.CharField(max_length=100)),
                ('anleitungsschritt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SBSInstructions.anleitungsschritt')),
            ],
        ),
        migrations.AddField(
            model_name='anleitung',
            name='profil',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='SBSInstructions.profil'),
        ),
    ]
