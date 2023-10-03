import requests
from .models import Team
from dotenv.main import load_dotenv
import os


LANG_ID = 1 # 21 - russian 1 - english
TIMEZONE = 'Europe/Moscow'
SPORT = 4 # 4 - hockey
KHL_ID = 636
NHL_ID = 366


load_dotenv()


def parse_result_match(date, team_1, team_2):
    """
    Receiving result of match from ids teams and date
    result:list = [score_of_team_1, score_of_team_2]
    """

    url = 'https://allscores.p.rapidapi.com/api/allscores/custom-scores'
    team_ids = str(team_1) + ',' + str(team_2) 
    league_id = Team.objects.filter(id_on_api=team_1).values('league').get()
    league_id = KHL_ID if league_id['league'] == 'KHL' else NHL_ID
    querystring = {'timezone':TIMEZONE, "competitions":league_id,
                   'langId':LANG_ID, "startDate":date,
                   "endDate":date, "competitorIds":team_ids
                   }

    headers = {
	'X-RapidAPI-Key': os.environ['X_RAPIDAPI_KEY'],
	'X-RapidAPI-Host': os.environ['X_RAPIDAPI_HOST']
    }
    result = []
    response = requests.get(url, headers=headers, params=querystring)
    response_dict = response.json()
    games = response_dict.get('games')
    for i in games:
        if i['awayCompetitor']['id'] == team_1 or i['awayCompetitor']['id'] == team_2:
            result.append(i['awayCompetitor']['score'])
            result.append(i['homeCompetitor']['score'])
            if len(i['shortStatusText'].split()) > 1:
                result.append(i['shortStatusText'].split()[1])
            elif i['shortStatusText'] != 'Sched.':
                result.append('main_time')
            else:
                result.append('Scheduled')
            
            
    

    return result



if __name__ == '__main__':
    id_1 = 8713
    id_2 = 8762
    date = '28/10/2022'
    print(parse_result_match(date, id_1, id_2))
