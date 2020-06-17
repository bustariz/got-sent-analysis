from flask import Flask,render_template,jsonify
from flask_pymongo import PyMongo
from bson.json_util import dumps, loads 
import data


app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/sent_analysisdb"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

@app.route("/")
def index():
    # data.run_functions()
    collection = mongo.db.got_scripts
    d = dumps(collection.find())

    # return render_template('index.html', d=d)
    return render_template('index.html', d=d)


if __name__ == "__main__":
    app.run(debug=True)