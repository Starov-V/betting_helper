# Generated by Django 4.2.5 on 2023-10-02 11:23

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('bet', '0004_alter_bet_result_alter_bet_type_of_bet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bet',
            name='result',
            field=models.PositiveSmallIntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='bet',
            name='type_of_bet',
            field=django_mysql.models.ListCharField(models.CharField(default=None, max_length=20, null=True), default=[None, None], max_length=42, size=2),
        ),
    ]
