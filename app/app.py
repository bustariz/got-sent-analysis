import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

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
# script = Base.classes.got_script

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
        f"/api/v1.0/text <br/>"
        f'/api/v1.0/sentiment'
    )

# @app.route('/api/v1.0/text')
# def text_analysis():
#       # Create our session (link) from Python to the DB
#     session = Session(engine)

#     """Return a list of all passenger names"""
#     # Query all passengers
#     results = session.query(script_table).all()

#     session.close()

#     all_names = list(np.ravel(results))

#     return jsonify(all_names)


# Use flask_pymongo to set up mongo connection
# app.config["MONGO_URI"] = "mongodb://localhost:27017/sent_analysisdb"
# mongo = PyMongo(app)

# data.run_functions()

# @app.route("/api/v1.0/text/season")
# def index():
#     collection = mongo.db.got_scripts

#     pipeline = [
#         {
#             "$group":{
#                 "_id":"$name",
#                 "total_word_count": {"$sum":"$word_count"},
#                 "avg_compound_score": {"$avg":"$compound_score"}
#             }
#         },
#         {
#             "$sort":{"total_word_count":-1}
#         },
#         {
#             "$limit": 100
#         }
#     ]

#     chars_word_count = collection.aggregate(pipeline=pipeline)
    
#     output = []
#     for item in chars_word_count:
#         output.append({
#             "name":item["_id"],
#             "total_word_count":item["total_word_count"],
#             "avg_compound_score": item["avg_compound_score"]
#             })

#     return jsonify({"results": output})



# @app.route("/api/v1.0/text/season/<string:season_num>")
# def season_text(season_num):

#     collection = mongo.db.got_scripts

#     pipeline = [
#         {
#             "$match":{"season":f"Season {season_num}"}
#         },
#         {
#             "$group":{
#                 "_id":"$name",
#                 "total_word_count": {"$sum":"$word_count"},
#                 "avg_compound_score": {"$avg":"$compound_score"}
#             }
#         },
#         {
#             "$sort":{"total_word_count":-1}
#         },
#         {
#             "$limit": 100
#         }
#     ]

#     chars_word_count = collection.aggregate(pipeline=pipeline)
    
#     output = []
#     for item in chars_word_count:
#         output.append({
#             "name":item["_id"],
#             "total_word_count":item["total_word_count"],
#             "avg_compound_score": item["avg_compound_score"]
#             })

#     return jsonify({"results": output})

# @app.route("/api/v1.0/text/season/all")
# def all_season_text():
    
#     collection = mongo.db.got_scripts

#     pipeline = [
#         {
#             "$group":{
#                 "_id":"$season",
#                 "total_word_count": {"$sum":"$word_count"},
#                 "avg_compound_score": {"$avg":"$compound_score"}
#             }
#         },
#         {
#             "$sort":{"total_word_count":-1}
#         },
#         {
#             "$limit": 100
#         }
#     ]

#     chars_word_count = collection.aggregate(pipeline=pipeline)
    
#     output = []
#     for item in chars_word_count:
#         output.append({
#             "season":item["_id"],
#             "total_word_count":item["total_word_count"],
#             "avg_compound_score": item["avg_compound_score"]
#             })

#     return jsonify({"results": output})




if __name__ == "__main__":
    app.run(debug=True)