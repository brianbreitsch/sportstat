
# REST API README

This REST aplication using MongoDB and Flask is based off the example from the MongoEngine website:
http://docs.mongoengine.org/projects/flask-mongoengine/en/latest/

There is a similar example at the MongoDB website:
https://docs.mongodb.org/ecosystem/tutorial/write-a-tumblelog-application-with-flask-mongoengine/


## Run

Following the example in the link at the beginning of this document, we run

    python manage.py runserver

to start the REST server.


### WARNING

By default, this application is serving on '0.0.0.0', which corresponds to all IPs in Flask.
As such, development should be on a private network.



## Organization

Models of this data *ARE NOT* defined in this module.  Rather, they are defined in the `sportstat` module.
As such, when using these models in the Flask application, they should be imported from the `sportstat` module:

    from sportstat.models import *


## Database

See the `README.md` in `sportstat/models` for detailed information about the mongodb setup.
The Flask application has configuration files (see `default_settings.cfg`) that tell MongoEngine on which IP/PORT the `mongod` process is listening.
