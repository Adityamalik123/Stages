
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import numpy
from numpy import genfromtxt

def Load_Data(file_name):
    data = genfromtxt(file_name, delimiter=',', skip_header=1,usecols = (0, 1, 2, 3, 4, 5), dtype=None)
    return data.tolist()

Base = declarative_base()

class First(Base):
    __tablename__ = 'First'
   
    pin = Column(String(250), primary_key=True)
    place = Column(String(250), nullable=True)
    address = Column(String(250), nullable=True)
    lat = Column(String(250), nullable=True)
    longi = Column(String(250), nullable=True)
    accuracy = Column(String(250), nullable=True)

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'pin'         : self.pin,
           'address'           : self.place,
           'city' : self.address,
           'latitude' : self.lat,
           'longitude' : self.longi
       }





if __name__=="__main__":
	engine = create_engine('postgresql+psycopg2://ziqrrxhtjdnwyx:477f3b70a91bb04a95d516b09073752f3c9d66573aca16d5734412b71bb50573@ec2-107-20-176-7.compute-1.amazonaws.com:5432/d8hdjvhg1njr3o')
 	Base.metadata.create_all(engine)
 	DBSession = sessionmaker(bind=engine)
	session = DBSession()
	file_name="IN.csv"
	data=Load_Data(file_name)
	for i in data:
		print i
		record=First(**{
			'pin':i[0],
			'place':i[1],
			'address':i[2],
			'lat':i[3],
			'longi':i[4],
			'accuracy':i[5]
			})
		session.add(record)
		session.commit()
		session.close()





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