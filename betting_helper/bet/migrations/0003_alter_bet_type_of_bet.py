# Generated by Django 4.2.5 on 2023-09-29 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bet', '0002_remove_bet_sport_bet_author_bet_date_of_match_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bet',
            name='type_of_bet',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]
