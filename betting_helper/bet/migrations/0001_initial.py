# Generated by Django 4.2.5 on 2023-09-25 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('league', models.CharField(choices=[('KHL', 'KHL'), ('NHL', 'NHL')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sport', models.CharField(choices=[('soccer', 'soccer'), ('basketball', 'basketball'), ('hockey', 'hockey')], default='hockey', max_length=100)),
                ('result', models.PositiveSmallIntegerField()),
                ('guest_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guest_team', to='bet.team')),
                ('home_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_team', to='bet.team')),
            ],
        ),
    ]
