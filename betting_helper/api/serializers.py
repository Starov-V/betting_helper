from rest_framework import serializers
from rest_framework.fields import empty
from bet.models import Bet, Team
from bet.calculate_bet import calculate


class BetSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    type_of_bet = serializers.ListField(
        min_length = 1,
        max_length = 2
    )

#    def get_result(self, obj):
#        home_team = Team.objects.filter(id=self.context.get('request').data['home_team']).get().id_on_api
#        guest_team = Team.objects.filter(id=self.context.get('request').data['guest_team']).get().id_on_api
#        date = self.context.get('request').data['date_of_match']
#        type_of_bet = self.context.get('request').data['type_of_bet']
#        return calculate(date, home_team, guest_team, type_of_bet)
    

    class Meta:
        model = Bet
        fields = ('id', 'home_team', 'guest_team', 'type_of_bet', 'date_of_match', 'author')
