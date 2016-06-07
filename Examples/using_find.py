#Examples of using find to query documents in a collection

import pymongo
import sys #For the Exception handle
import datetime

try:
	# Establish a connection to the database:
	connection = pymongo.MongoClient("mongodb://localhost") # running server on localhost
	#Get handle to the school database
	db = connection.school #connection to school db
	scores = db.scores #scores collections
	print "Successfully connected to MongoDB..."

except Exception as e:
	print "Did not connect to the MongoDB...", type(e), e

def find_one():
	print "Implementing Find One:"
	query = {'student_id':10} #looking for document with id = 10

	try:
		doc = scores.find_one(query) #return single document
	
	except Exception as e:
		print "Unexpected error:", type(e), e

	print doc

def find_query():
	query = {"type": 'exam','score':{'$gte':80, '$lte':100}}
	projection = {"student_id":1,"score":1,"_id":0} #1 = include; 0 = exclude
	
	try:
		cursor = scores.find(query,projection) #cursor b/c multiple queries returned

	except Exception as e:
		print "Unexpected error:", type(e), e

	sanity = 0
	for doc in cursor:
		print doc
		# controllig how many documents are returned
		sanity +=1
		if sanity > 10:
			break

def sort_skip_limit():
	# Order: Sort, Skip, Limit
	# as a note: the query doesn't begin until you iterate through the cursor:
	query = {}
	projections = {'type':0,'_id':0}
	# assign cursor
	cursor = scores.find(query,projections).skip(2) #skip
	cursor = cursor.limit(5) #limit
	cursor = cursor.sort([('student_id',pymongo.ASCENDING),('score',pymongo.DESCENDING)]) #sort

	#Example of single line
	#cursor = scores.find().sort([('student_id',pymongo.ASCENDING),('score', pymongo.DESCENDING)]).skip(3).limit(15)
	
	#iterate and print:
	for doc in cursor:
		print doc

def insert_one():
	# insert student info
	db = connection.school
	people = db.people

	kate = {"Name": "Kate Degatur", "Company":"LSU",
			"Interest": ['hores','biking','reading']}
	trace = {"Name": "Trace Smith", "Company": "Udacity",
			"Interest":['running','python','hiking']}
	scott = {"Name": "Scott Whitford","Company":"LSU",
			"Interest": ['cooking','reading','running']}

	try:
		people.insert_one(trace)
		#del(trace['_id'])

	except Exception as e:
		print "Unexpected error:", type(e), e

	print()

def insert_many():
	# insert student info
	db = connection.school
	people = db.people

	kate = {"Name": "Kate Degatur", "Company":"LSU",
			"Interest": ['hores','biking','reading']}
	trace = {"Name": "Trace Smith", "Company": "Udacity",
			"Interest":['running','python','hiking']}
	scott = {"Name": "Scott Whitford","Company":"LSU",
			"Interest": ['cooking','reading','running']}
	people_to_insert = [kate,trace]
	
	try:
		people.insert_many(people_to_insert,order=True)

	except Exception as e:
		print "Unexpected error:", type(e), e

def add_review_date_using_update_one(student_id):
	db = connection.school
	scores = db.scores

	try:
		# get the document
		score = scores.find_one({'student_id':student_id,'type':'exam'})
		print "Before: ", score

		#update using set to change score:
		record_id = score['_id']
		result = scores.update_one({'_id':record_id},
			{'$set':{'review_date':datetime.datetime.utcnow()}})

		print "Number of Matches: ", result.matched_count

		score = scores.find_one({'_id':record_id})
		print "New Score: ", score

	except Exception as e:
		print "Unexpected error:", type(e), e

def add_review_date_for_all():
	db = connection.school
	scores = db.scores

	try:
		result = scores.update_many({},
			{'$set':{'review_date':datetime.datetime.utcnow()}})

		print "Number of Matches: ", result.matched_count

	except Exception as e:
		print "Unexpected error:", type(e), e

def run():
	"""Run the following scripts"""
	#find_one()
	#find_query()
	#sort_skip_limit()
	#insert_one()
	#insert_many()
	#add_review_date_using_update_one(1)
	add_review_date_for_all()

if __name__ == "__main__":
	run()