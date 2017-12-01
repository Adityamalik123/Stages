import os, httplib2, sys, json
import unittest
class FlaskTestCase(unittest.TestCase):
	
	def test_server_is_up_and_running_get_using_self(self):
		print "Running Tester for self getting....\n"
		address = raw_input("Please enter the address of the server you want to access, \n If left blank the connection will be set to 'http://localhost:5000':   ")
		if address == '':
			address = 'http://localhost:5000'
			#Making a Request
			print "Making a request to /get_location..."
			try:
				url = address + "/get_using_self?location=31.2834+74.7797"
				h = httplib2.Http()
				resp, result = h.request(url, 'GET')
				obj = json.loads(result)
				new = obj['Pin_Codes']
				if resp['status'] != '200':
					raise Exception('Received an unsuccessful status code of %s' % resp['status'])
			except Exception as err:
				print "Test 1 FAILED: Could not make GET Request to web server"
				print err.args
				sys.exit()
			else:
				print "Test 1 PASS: Succesfully Made GET Request to /get_using_self"

if __name__ == '__main__':
	unittest.main()
