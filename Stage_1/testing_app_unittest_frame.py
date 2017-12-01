import os, httplib2, sys, json
import unittest
class FlaskTestCase(unittest.TestCase):
	
	def test_server_is_up_and_running_post(self):
		print "Running Tester....\n"
		address = raw_input("Please enter the address of the server you want to access, \n If left blank the connection will be set to 'http://localhost:5000':   ")
		if address == '':
			address = 'http://localhost:5000'
			#Making a Request
			print "Making a post request to /post_location..."
			try:
				url = address + "/post_location?location=28.6488+77.1726+110085+rohini+delhi"
				h = httplib2.Http()
				resp, result = h.request(url, 'POST')
				obj = json.loads(result)
				new = obj['Exists_Already']['pin']
				if new != "110085":
					print "No.... Its a wrong Answer"
				if resp['status'] != '200':
					raise Exception('Received an unsuccessful status code of %s' % resp['status'])
			except Exception as err:
				print "Test 2 FAILED: Could not make POST Request to web server"
				print err.args
				sys.exit()
			else:
				print "Test 2 PASS: Succesfully Made POST Request to /post_location"


	def test_server_is_up_and_running_get(self):
		print "Running Tester....\n"
		address = raw_input("Please enter the address of the server you want to access, \n If left blank the connection will be set to 'http://localhost:5000':   ")
		if address == '':
			address = 'http://localhost:5000'
			#Making a Request
			print "Making a get request to /get_location..."
			try:
				url = address + "/get_location?pin=110085"
				h = httplib2.Http()
				resp, result = h.request(url, 'GET')
				obj = json.loads(result)
				new = obj['First']['address']
				if new != "rohini":
					print "No.... Its a wrong Answer"
				if resp['status'] != '200':
					raise Exception('Received an unsuccessful status code of %s' % resp['status'])
			except Exception as err:
				print "Test 1 FAILED: Could not make GET Request to web server"
				print err.args
				sys.exit()
			else:
				print "Test 1 PASS: Succesfully Made GET Request to /get_location"


if __name__ == '__main__':
	unittest.main()
