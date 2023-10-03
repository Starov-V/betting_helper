from django.db import models
from users.models import User
from django.utils import timezone
from django_mysql.models import ListCharField

class Team(models.Model):
    """
    Describe details of team.
    """
    LEAGUE_CHOICES = (
        ('KHL','KHL'),
        ('NHL', 'NHL')
    )
    name = models.CharField(
        max_length=100
    )
    league = models.CharField(
        choices=LEAGUE_CHOICES,
        max_length=100
    )
    id_on_api = models.IntegerField(
        null=True
    )

    def __str__(self) -> str:
        return self.name


class Bet(models.Model):
    """
    Describe details of bet
    """
    TYPES_OF_BET_CHOICES = (
        ('home_win','home_win'),
        ('guest_win','guest_win'),
        ('over_more','over_more'),
        ('over_less','over_less'),
        ('in_match', 'in_match')
    )
    RESULTS_CHOICES = (
        (1,'win'),
        (0,'returned'),
        (-1,'lose'),
        (2, 'not calculated')
    )
    home_team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name='home_team'
    )
    guest_team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name='guest_team'
    )
    type_of_bet = ListCharField(
        base_field=models.CharField(
            max_length=20,
            default=None,
            null=True,
        ),
        size=2,
        max_length=(2*21),
        default=[None, None]

        
    )
    date_of_match = models.DateField(
        auto_now=False,
        default=timezone.now
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='bets',
        default=None,
        null=True
    )
    result = models.PositiveSmallIntegerField(
        default=2,
        choices=RESULTS_CHOICES
    )

    def __str__(self) -> str:
        return f'{self.home_team} - {self.guest_team} ({self.date_of_match}) - {self.type_of_bet} - {self.result}'
