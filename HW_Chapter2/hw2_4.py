'''Which of the choices below is the title of a movie from the year 2013 that 
is rated PG-13 and won no awards? Please query the video.movieDetails collection 
to find the answer.'''

import pymongo
import sys

#Loading in the dump file to Mongodb
# In the terminal type: mongorestore --drop -d movies -c movieDetails movieDetails.bson

try:
	connection = pymongo.MongoClient("mongodb://localhost")
except Exception as e:
	print "Unexpected Error: ", type(e), e

def movie_query1():
	#Homework Question 2.3
	db = connection.movies
	movieDetails = db.movieDetails
	query = {'year':2013, 'awards.wins':0,'rated':'PG-13'}
	projection = {'title':1, '_id':0}
	try:
		doc = db.movieDetails.find(query,projection)
	
	except Exception as e:
		print "Unexpected Error: ", type(e), e

	for item in doc:
		print item 

	print ""

def movie_query2():
	# Additional Query:
	db = connection.movies
	movieDetails = db.movieDetails
	query = {'rated':'PG-13','year':{'$lte':2014}, 'genres':{'$all':["Documentary"]}}
	projection = {'title':1, '_id':0}
	try:
		doc = db.movieDetails.find(query,projection)
	
	except Exception as e:
		print "Unexpected Error: ", type(e), e

	print "*** All Movies Before 2010: ***"
	for item in doc:
		print item 

def run():
	movie_query1()
	movie_query2()

if __name__ == "__main__":
	run()