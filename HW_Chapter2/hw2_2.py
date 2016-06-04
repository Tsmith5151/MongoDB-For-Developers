
'''Write a program in the language of your choice that will remove the grade of type "homework" 
with the lowest score for each student from the dataset in the handout. Since each document is 
one grade, it should remove one document per student.'''

import pymongo
import sys

# Establish a connection to the database:
try:
	connection = pymongo.MongoClient("mongodb://localhost")

except Exception as e: #raise error if cannot connect to db
	print "Unexpected Error: ", type(e), e
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
				grades.remove({'student_id': doc['student_id']})

def run():
	question_2()

if __name__ == "__main__":
	run()
