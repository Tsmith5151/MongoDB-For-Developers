'''Find all exam scores greater than or equal to 65, and sort those scores from lowest to highest.
What is the student_id of the lowest exam score above 65?'''

import pymongo
import sys

#Connect to the database
try:
	connection = pymongo.MongoClient("mongodb://localhost")

except Exception as e: #raise error if cannot connect to db
	print "Unexpected Error: ", type(e), e

def question_1():
	db = connection.students #connect to the students db
	grades = db.grades #grades collection
	projections = {'_id':0}
	cursor = db.grades.find({'type':'exam','score':{'$gte': 65}})
	cursor = cursor.sort('score',pymongo.ASCENDING) 
	for item in cursor:
		print item

def question_2():
	#First task is to find which student has the highest average in the class
	db = connection.students
	grades = db.grades
	
	try:
		cursor = grades.find({'type':'homework'},{'_id':0}).sort([('student_id',pymongo.ASCENDING),('score',pymongo.ASCENDING)]).limit(5)

	except Exception as e:
		print "Unexpected Error: ", type(e), e

	previous_id = None
	student_id = None

	for doc in cursor:
			student_id = doc['student_id']
			if student_id != previous_id:
				previous_id = student_id
				print "Removing", doc
				grades.remove({'_id': doc['student_id']})

def run():
	#question_1()
	question_2()

if __name__ == "__main__":
	run()
