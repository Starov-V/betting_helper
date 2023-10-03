from .parcing_results import parse_result_match
from .models import Team, Bet
from datetime import datetime

def parse_db():
    TODAY = datetime.date()
    bets = Bet.objects.filter(result=2, date_of_match__gt=TODAY).prefetch_related()
    for bet in bets:
        home_team = bet.home_team.id_on_api
        guest_team = bet.guest_team.id_on_api
        date = bet.date_of_match
        type_of_bet = bet.type_of_bet
        bet.result = calculate(date, home_team, guest_team, type_of_bet)       
        bet.save()

def calculate(home_team, guest_team, date, bet):
    result_match = parse_result_match(home_team, guest_team, date)
    if result_match[2] == 'Scheduled':
        return 2
    type_of_bet = bet[0]
    func = globals()[type_of_bet]
    return(func(result_match)) if len(bet) == 1 else func(result_match, bet[1])
    

def home_win(result, condition):
    score_1, score_2, fact = result
    if not condition == 'in_match':
        if fact != 'main_time':
            return -1
    if score_1 > score_2:
        return 1
    return -1
    



def guest_win(result, condition):
    score_1, score_2, fact = result
    if not condition == 'in_match':
        if fact != 'main_time':
            return -1
    if score_1 < score_2:
        return 1
    return -1


def over_more(result, goal):
    score_1, score_2, _ = result
    if not goal - int(goal):
        if score_1 + score_2 == goal:
            return 0
    if score_1 + score_2 > goal:
        return 1
    return -1


def over_less(result, goal):
    score_1, score_2, _ = result
    if not goal - int(goal):
        if score_1 + score_2 == goal:
            return 0
    if score_1 + score_2 < goal:
        return 1
    return -1


if __name__ == '__main__':
    parse_db()
