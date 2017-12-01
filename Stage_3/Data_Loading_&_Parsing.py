from flask import Flask
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

with open('data.json') as json_data:
	d=json.load(json_data)
	for l in d['features']:
		name=l['properties']['name']
		paent=l['properties']['parent']
		for j in l['geometry']['coordinates'][0]:
			new = Second(lat=j[0], longi=j[1], place1=name, place2=paent)
			session.add(new)
			session.commit()



if __name__ == '__main__':
  app.secret_key = 'super_secret_key'
  app.debug = True