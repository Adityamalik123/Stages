from flask import Flask, render_template, request,jsonify
app = Flask(__name__)

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from Database_setup_with_CSV_Loading import First, Base
from sqlalchemy import func
import pandas as pd
from math import radians, cos, sin, asin, sqrt
#Connect to Database and create database session
engine = create_engine('postgresql+psycopg2://ziqrrxhtjdnwyx:477f3b70a91bb04a95d516b09073752f3c9d66573aca16d5734412b71bb50573@ec2-107-20-176-7.compute-1.amazonaws.com:5432/d8hdjvhg1njr3o')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

#JSON APIs to find the pin codes withi 5 km radius
@app.route('/get_using_self')
def self_get():
	location = request.args.get('location')
	listi=[]
	loc=location.split()
	lat1=float(loc[0])
	long1=float(loc[1])	
	places=session.query(First).all()
	for i in places:
		try:
			lat2=float(i.lat)
			long2=float(i.longi)
		except ValueError:
			continue
		lat1=float(loc[0])
		long1=float(loc[1])
		lat1=radians(lat1)
		long1=radians(long1)
		lat2=radians(lat2)
		long2=radians(long2)
		dlong=long2-long1
		dlat=lat2-lat1
		a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlong/2)**2
		c = 2 * asin(sqrt(a)) 
		r = 6371
		if c*r <= 5:
			print i.pin
			listi.append(i.pin) 
	return jsonify(Pin_Codes=listi)

if __name__ == '__main__':
  app.secret_key = 'super_secret_key'
  app.debug = True
  app.run(host = '0.0.0.0', port = 5000)

