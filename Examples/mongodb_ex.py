#Clear Port 
#ps -fA | grep python

import bottle
import pymongo as py 

@bottle.route('/') #Default route of webserver

def index():
	#connect to the database
	connection = py.MongoClient('localhost', 27017) #Default port
	# connect to test database
	db = connection.test 
	
	#Handle to names Collection
	names = db.names 
	#finds a single document
	item = names.find_one()
	#return what is in the names key of the document
	return '<b>Hello %s!</b>' % item['name']
	
bottle.run(host = 'localhost', port=8082)