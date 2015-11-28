
# MongoDB

## Usage

In order to use mongodb, import models from application before calling:

    from mongoengine import connect
    connect(name, hostname, port)

The mongo models will then behave as expected and save/find will operate on the connected db.


# DB Creation

The tutorial here was used in creating the database:
http://www.tutorialspoint.com/mongodb/mongodb_create_database.htm

Our `DATABASE_NAME` is `sportstatdb` and is hardcoded into the Flask app initialization.

In order to use/test this project on a new machine, you will need to have mongo running on the machine.
You will also need to create a database.
After launching `mongo` in the shell, run the following command:

    use sportstatdb

Then run:

    db.serverCmdLineOpts()

to see which IP and port mongo is listening on for the machine.
(TODO: someone else started mongo on my work machine, so I don't actually know about starting mongo cold).
