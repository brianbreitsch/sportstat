
import os
from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_object('sportstat_server.default_settings')

if os.getenv('SERVER_SETTINGS') is not None:
    app.config.from_envvar('SERVER_SETTINGS')

db = MongoEngine(app)

from sportstat_server import rest

if __name__ == '__main__':
    app.run()

