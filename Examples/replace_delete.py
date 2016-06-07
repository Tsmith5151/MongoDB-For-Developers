import pymongo
import sys
import datetime

try:
	connection = pymongo.MongoClient("mongodb://localhost")

except Exception as e:
	print "Unexpected Error: ", type(e), e

def remove_review_dates():
	db = connection.school
	scores = db.scores
	try:
		result = scores.update_many({'review_date':{'$exists': True}},
									{'$unset': {'review_date':1}})
		print "Mathched number of docs: ", result.matched_count
	except Exception as e:
		print "Unexpected Error: ", type(e), e

def replace_one(student_id):
	#Adding review Date
	db = connection.school
	scores = db.scores

	try:
		score = scores.find_one({'student_id':student_id,'type':'exam'}) #call find one into var
		print "Before: ", score

		#add a review_date
		score['review_date'] = datetime.datetime.utcnow() #set new key w/ value

		#Update document by calling replace_one
		record_id = score['_id'] #pulling out _id from the document taken from the server
		scores.replace_one({'_id':record_id},score) #ammend doc
		score = scores.find_one({'_id':record_id})
		print "After: ", score

	except Exception as e:
		print "Unexpected Error: ", type(e), e

def delete_one(student_id):
	# Remove a student from the school collections
	db = connection.school
	scores = db.scores

	try:
		#results = scores.delete_one({'student_id':student_id}) 
		results = scores.delete_many({'student_id':student_id}) 
		print "Searching for student with id '%s' to delte: " % (student_id)
		print "Number of deleted docs: ", results.deleted_count
	except Exception as e:
		print "Unexpected Error: ", type(e), e

def find_student_data(student_id):
	#search for student based on id
	db = connection.school
	scores = db.scores
	try:
		doc = scores.find({'student_id':student_id})
	except Exception as e:
		print "Unexpected Error: ", type(e), e
	
	for item in doc:
		print doc #shouldn't print anything out if properly deleted

def run():
	#remove_review_dates()
	#replace_one(1)
	delete_one(1)
	find_student_data(1)

if __name__ == "__main__":
	run()