from sportstat_server import app
from sportstat.models import Team, Athlete, Game, Play, Action, Observation


@app.route('/')
def home():
    '''
    Tell the user they've accessed the SportStat server.
    '''
    return '''<h1>SportStat Server REST API</h1><br><p>See <a href="/help">help</a> for API help.</p>'''

@app.route('/help', methods=['GET'])
def api_help():
    '''
    Return help message and API usage/documentation.
    '''
    return '''<h1>Help Page</h1>'''

# @app.route('/sportstat/api/v0.1/athletes', methods=['GET'])
# def get_athletes():
#     '''
#     Return all athlete data in json format.
#     '''
#     athletes = [athlete.serialize for athlete in Athlete.objects.get()]
#     return jsonify(athletes)
# 
# @app.route('/sportstat/api/v0.1/athletes/<first>-<last>', methods=['GET'])
# def get_athlete_by_name(last, first=None):
#     '''
#     Return data in json format for athlete with corresponding name.
#     '''
#     athletes = [athlete.serialize for athlete in Athlete.objects.get(first=first, last=last)]
#     return jsonify(athletes)
# 
# @app.route('/sportstat/api/v0.1/athletes/<team>-<int:number>-<date>', methods=['GET'])
# def get_athlete_by_team_number_date(team, number, date=None):
#     '''
#     Return data in json format for athlete with corresponding team and number.
#     Optional date parameter can help resolve ambiguity.
#     '''
#     athletes = [athlete.serialize for athlete in Athlete.objects.get(team=team, number=number)]
#     return jsonify(athletes)
# 
# 
# 
# @app.route('/sportstat/api/v0.1/teams', methods=['GET'])
# def get_teams():
#     '''
#     Return all team data in json format.
#     '''
#     teams = [team.serialize for team in session.query(Team)]
#     return jsonify(teams)


