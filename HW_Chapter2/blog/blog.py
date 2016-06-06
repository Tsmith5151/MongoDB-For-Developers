import bottle

@bottle.route('/')
def home_page():
	mythings = ["apple","golf","football"]
	return bottle.template('template', username = 'Tsmith', things = mythings)

bottle.debug(True)
bottle.run(host = 'localhost', port = 8080)