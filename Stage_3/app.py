from flask import Flask, jsonify, request
app = Flask(__name__)

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from Database_Setup import Second, Base
import json

#Connect to Database and create database session
engine = create_engine('postgresql+psycopg2://swwjoagfckpota:1a43ae11ab48c20ac5493ca16aca4f0931ae5d1b7002d8ebcbd682dfef474047@ec2-54-247-120-234.eu-west-1.compute.amazonaws.com:5432/d8t6d3aobr94dd')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()
					


@app.route('/get_location', methods=['GET','POST'])
def restaurantMenuJSON12():
	location = request.args.get('location')
	if location:
		loc=location.split()
		restaurant = session.query(Second).filter_by(lat=loc[0], longi=loc[1]).first()
		if restaurant:
			return jsonify(Found=restaurant.serialize)
	return jsonify(Not_Present={
			'location':'Not Found'
			})


if __name__ == '__main__':
  app.secret_key = 'super_secret_key'
  app.debug = True
  app.run(host = '0.0.0.0', port = 5000)