import pymongo
import sys

'''How many movies list "Sweden" second in the the list of countries'''

# Establish a connection to the database:
try: 
	connection = pymongo.MongoClient("mongodb://localhost")

except Exception as e:
	print "Unexpected Error: ", type(e), e

def movie_query():
	#Get handle to the movies database
	db = connection.movies
	movieDetails = db.movieDetails #movieDetails collection
	query = {'countries.1':'Sweden'}
	projection = {'title':1,'_id':0}
	try:
		doc = movieDetails.find(query,projection)
		print "Total Number of Movies: ", doc.count()

	except Exception as e:
		print "Unexpected Error: ", type(e), e

def run():
	movie_query()

if __name__ == "__main__":
	run()