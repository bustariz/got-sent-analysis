import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, desc, asc
from sqlalchemy.sql.expression import cast

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
def chars_data():
      # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all passengers
    results = (
            session.query(script.name, func.avg(script.polarity_score), func.avg(script.subjectivity_score))
            .group_by(script.name)
            .order_by(asc(script.name))
            .all()
        )

    session.close()

    all_names = list(np.ravel(results))

    return jsonify(all_names)


@app.route('/api/v1.0/season/<string:season_num>')
def season_data(season_num):
      # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all passengers
    results = (
            session.query(script.name, func.avg(script.polarity_score), func.sum(cast(script.word_count,sqlalchemy.Integer)))
            .group_by(script.name,script.word_count)
            .order_by(desc(script.word_count))
            .filter(script.season == f'Season {season_num}')
            .all()
        )

    # results = session.query(script.name, func.sum(cast(script.word_count,sqlalchemy.Integer))).filter(script.season == f'Season {season_num}').group_by(script.name).all()

    session.close()

    all_names = list(np.ravel(results))

    return jsonify(all_names)

@app.route('/api/v1.0/season/all')
def all_data():
      # Create our session (link) from Python to the DB
    session = Session(engine)
 
    """Return a list of all passenger names"""
    # Query all passengers
    results = (
            session.query(script.season, func.avg(script.polarity_score), func.avg(script.subjectivity_score))
            .group_by(script.season)
            .order_by(asc(script.season))
            .all()
        )

    session.close()

    all_names = list(np.ravel(results))

    return jsonify(all_names)    


if __name__ == "__main__":
    app.run(debug=True)