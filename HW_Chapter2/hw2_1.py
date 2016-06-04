'''Find all exam scores greater than or equal to 65, and sort those scores from lowest to highest.
What is the student_id of the lowest exam score above 65?'''

import pymongo
import sys

# Establish a connection to the database:
try:
	connection = pymongo.MongoClient("mongodb://localhost")

except Exception as e: #raise error if cannot connect to db
	print "Unexpected Error: ", type(e), e

def question_1():
	#Get handle to the student database
	db = connection.students
	grades = db.grades #grades collection
	projections = {'_id':0}
	
	try: 
		cursor = db.grades.find({'type':'exam','score':{'$gte': 65}})
		cursor = cursor.sort('score',pymongo.ASCENDING) 
	except Exception as e:
		print "Unexpected Error: ", type(e), e

	for item in cursor:
		print item

def run():
	question_2()

if __name__ == "__main__":
	run()