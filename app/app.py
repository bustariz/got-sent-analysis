import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, desc, asc

from flask import Flask, render_template, jsonify

# from flask_cors import CORS
# import data

#################################################
# Database setup
#################################################
engine = create_engine('postgresql://postgres:bru1014ustz91@localhost/got_db')

# reflect existing db into new model
Base = automap_base()

# reflect tables
Base.prepare(engine,reflect = True)

# # ref to the table
script = Base.classes.got_script

#################################################
# flask setup
#################################################
app = Flask(__name__)
# CORS(app)

#################################################
#flask routes
#################################################

@app.route('/')
def welcome():
    """list all available API routes."""
    # return 'Hello World!'
    return (
        f"Available Routes: <br/>"
        f"/api/v1.0/chars <br/>"
        f'/api/v1.0/season/<season_num> <br/>'
        f'/api/v1.0/season/all <br/>'
    )

@app.route('/api/v1.0/chars')
def text_analysis():
      # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all passengers
    results = session.query(script.name, func.avg(script.polarity_score), func.avg(script.subjectivity_score)).group_by(script.name).order_by(asc(script.name)).all()

    session.close()

    all_names = list(np.ravel(results))

    return jsonify(all_names)


@app.route('/api/v1.0/season/<string:season_num>')
def text_analysis():
      # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all passengers
    results = session.query(script.name, func.avg(script.polarity_score), func.avg(script.subjectivity_score)).group_by(script.name).order_by(asc(script.name)).all()

    session.close()

    all_names = list(np.ravel(results))

    return jsonify(all_names)

@app.route('/api/v1.0/season/all')
def text_analysis():
      # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all passengers
    results = session.query(script.name, func.avg(script.polarity_score), func.avg(script.subjectivity_score)).group_by(script.name).order_by(asc(script.name)).all()

    session.close()

    all_names = list(np.ravel(results))

    return jsonify(all_names)    


if __name__ == "__main__":
    app.run(debug=True)