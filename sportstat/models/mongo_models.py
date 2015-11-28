
from sportstat_server import db



# TODO move this information to static files somewhere
STATES_AND_PROVINCES = (
        'AL', 'AK', 'AZ', 'AR', 'CA',
        'CO', 'CT', 'DE', 'FL', 'GA',
        'HI', 'ID', 'IL', 'IN', 'IA',
        'KS', 'KY', 'LA', 'ME', 'MD',
        'MA', 'MI', 'MN', 'MS', 'MO',
        'MT', 'NE', 'NV', 'NH', 'NJ',
        'NM', 'NY', 'NC', 'ND', 'OH',
        'OK', 'OR', 'PA', 'RI', 'SC',
        'SD', 'TN', 'TX', 'UT', 'VT',
        'VA', 'WA', 'WV', 'WI', 'WY',
        
        'AS', 'DC', 'FM', 'GU', 'MH',
        'MP', 'PW', 'PR', 'VI', 'AE',
        'AA', 'AE', 'AP')

POSITIONS = (
        ('QB', 'quarterback'),
        ('TE', 'tight end'),
        )


class Athlete(db.Document):
    position = db.StringField(choices=POSITIONS)
    first_name = db.StringField(max_length=80, required=True)
    last_name = db.StringField(max_length=80, required=True)


class Team(db.Document):
    name = db.StringField(primary_key=True, unique=True, max_length=80)
    city = db.StringField(max_length=80)
    state = db.StringField(choices=STATES_AND_PROVINCES)
    roster = db.ListField(ReferenceField(db.Athlete), default=list)


class Game(db.Document):
    home_team = db.ReferenceField(Team)
    away_team = db.ReferenceField(Team)
    datetime = db.DateTimeField()
    location = db.StringField(max_length=80)


class Play(db.Document):
    play_index = db.IntField(required=True)
    quarter_index = db.IntField(required=True)
    down = db.IntField(required=True)
    offense = db.ReferenceField(Team)
    defense = db.ReferenceField(Team)
    half = db.BooleanField()
    yards = db.IntField()
    result = db.StringField(max_length=40)


class Observation(db.Document):
    name = db.StringField(max_length=40)
    value = db.StringField(max_length=80)


class Action(db.Document):
    action_type = db.StringField(max_length=80)
    player = db.ReferenceField(Athlete)
    observations = db.ListField(Observation(), default=list)

