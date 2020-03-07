import datetime as dt
import numpy as np
import sqlalchemy
import scrape_mars
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo

# Flask startup
app = Flask(__name__)

# Connect to Mongo
mongo = PyMongo(app, uri="mongodb://localhost:27017/scraper")

# Home page w data from Mongo
@app.route("/")
def home():
    # Grab a row
    space_stuff = mongo.db.mars.find_one()

    # Return jinja template
    return render_template("index.html", space_stuff=space_stuff)

# Scrape method 
@app.route("/scrape")
def scrape():

    # Scrape!
    space_stuff = scrape_mars.scrape()

    # Delete previously stored data
    mongo.db.mars.drop()

    # Upsert Mongo
    mongo.db.mars.insert(space_stuff)

    # Redirect user to home 
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)