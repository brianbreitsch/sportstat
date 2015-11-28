# Sports Statistics Data Analysis
===============================


A Python module for parsing and analyzing sports statistics.


# Development

## Install and Setup

### Packages and Dependencies

*kind of optional*

1. create and activate a virtual environment

    - for vanilla Python:

    $ pip install virtualenv
    $ virtualenv sportstat
    $ source sportstat/bin/activate

    - with Anaconda:

    $ conda create -n sportstat anaconda
    $ source activate sportstat

Note: when using Anaconda, you may choose to limit the packages to just those
indicated in the requirements.txt file by specifying:

    $ conda create -n sportstat --file requirements.txt

For developers; to update requirements.txt after installing packages (using 
pip or conda install), run:

    $ conda list -e > requirements.txt

to overwrite the requirements file.


2. Install dependencies

    $ pip install -r requirements.txt


3. Install `sportstat` python package

    - first build the package:

    $ python setup.py build

    - then, if only deploying (not developing):

    $ python setup.py install

    - if developing or testing:

    $ python setup.py develop


The module `sportstat` contains useful query and analysis functions along with Mongo document models.
The module `sportstat_server` contains a Flask application for serving the data REST API.

TODO: There is an interdependency--because MongoEngine uses Flask for its configuration, and we want the same MongoEngine wrapper when working on
analytics and on the REST server, we end up pulling the MongoEngine `db` instance from the `sportstat_server` module into the `models` module when
defining the Mongo document models.  This should not be a problem as long as these two projects are together.




# Notebooks

To analyze/parse data using jupyter notebooks, make sure your jupyter instance is running in the same environment that you installed `sportstat` and `sportstat_server`.


