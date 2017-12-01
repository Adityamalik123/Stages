from flask import Flask, request, jsonify
app = Flask(__name__)

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from Database_setup_with_CSV_Loading import First, Base


#Connect to Database and create database session
engine = create_engine('postgresql+psycopg2://ziqrrxhtjdnwyx:477f3b70a91bb04a95d516b09073752f3c9d66573aca16d5734412b71bb50573@ec2-107-20-176-7.compute-1.amazonaws.com:5432/d8hdjvhg1njr3o')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

#JSON APIs to view Information through pincode
@app.route('/get_location')
def getLocation():
	pincode = request.args.get('pin')
	restaurant = session.query(First).filter_by(pin = "IN/"+pincode).first()
	if restaurant:
		return jsonify(First=restaurant.serialize)
	return jsonify(First={
		'pin':'not found'
		})

#JSON APIs to post Information 
@app.route('/post_location', methods=['POST'])
def postLocation():
	location = request.args.get('location')
	loc=location.split()
	restaurant = session.query(First).filter_by(pin = "IN/"+loc[2]).first()
	if restaurant:
		return jsonify(Exists_Already=restaurant.serialize)
	new = First(pin="IN/"+loc[2], lat=loc[0], longi=loc[1], place=loc[3], address=loc[4], accuracy=None)
	session.add(new)
	session.commit()
	rest = session.query(First).filter_by(pin = "IN/"+loc[2]).first()
	return jsonify(Added=rest.serialize)


if __name__ == '__main__':
  app.secret_key = 'super_secret_key'
  app.debug = True
  app.run(host = '0.0.0.0', port = 5000)

