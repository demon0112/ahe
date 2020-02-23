from flask import Flask
from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from flask import request,redirect
from flask import current_app
from datetime import datetime
from flask import jsonify
import simplejson as json
import os
import psycopg2
import json
basedir = os.path.abspath(os.path.dirname(__file__))#connection with database
get=Flask(__name__)
get.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:demon0112@localhost/ahe'
get.debug=True
db = SQLAlchemy(get)
conn = psycopg2.connect(database = 'ahe', user = 'postgres', password = 'demon0112', host = 'localhost')
curs = conn.cursor()
# Creating our database model
class Solar(db.Model):
    __tablename__ = "solarpower"
    ts = db.Column(db.DateTime(), primary_key=True)
    solarpower = db.Column(db.Float())
    __tablename__ = "loadpower"
    ts = db.Column(db.DateTime(), primary_key=True)
    loadpower = db.Column(db.Float())
@get.route('/')   
def home():
    return render_template('index.html')
@get.route('/minute_solar_power')
def minute_solar_power():
     curs.execute("select * from solarpower ")
     rows=curs.fetchall() 
     return jsonify({"results" : rows})
@get.route('/minute_load_power')
def minute_load_power():
     curs.execute("select * from loadpower ")
     rows=curs.fetchall() 
     return jsonify({"results" : rows})
@get.route('/hourly_solar_power')
def hourly_solar_power():
     curs.execute("select date_trunc('hour' , ts) as t , sum(cast (solarpower as float )/60) from solarpower group by t order by t asc")
     rows=curs.fetchall() 
     return jsonify({"results" : rows})
@get.route('/hourly_load_power')
def hourly_load_power():
     curs.execute("select date_trunc('hour' , ts) as t , sum(cast (loadpower as float )/60) from loadpower group by t order by t asc")
     rows=curs.fetchall() 
     return jsonify({"results" : rows})

     
     

if __name__=="__main__":
    get.run()
   