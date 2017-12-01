'''from flask import g
import psycopg2
from psycopg2.extras import DictCursor
import csv
'''
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Second(Base):
    __tablename__ = 'Second'
   
    id = Column(Integer, primary_key=True)
    place1 = Column(String(250), nullable=True)
    place2 = Column(String(250), nullable=True)
    lat = Column(String(250), nullable=True)
    longi = Column(String(250), nullable=True)

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'name'         : self.place1,
           'parent'           : self.place2,
           'latitude' : self.lat,
           'longitude' : self.longi
       }





if __name__=="__main__":
	engine = create_engine('postgresql+psycopg2://swwjoagfckpota:1a43ae11ab48c20ac5493ca16aca4f0931ae5d1b7002d8ebcbd682dfef474047@ec2-54-247-120-234.eu-west-1.compute.amazonaws.com:5432/d8t6d3aobr94dd')
 	Base.metadata.create_all(engine)
 	


'''

def init_admin():
	db=connect
	with open('IN.csv', 'r') as f:
		reader = csv.reader(f)
		next(reader)  # Skip the header row.
		for row in reader:
			db[1].execute(
				"INSERT INTO first (pin, place, address, lat, long, accuracy) VALUES (%s, %s, %s, %s, %s, %s)", row)
	db[1].close()
	db[0].close()

if __name__=='__main__':
	init_db()
	init_admin()
	'''