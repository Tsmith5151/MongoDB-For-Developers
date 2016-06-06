'''Type the following in the terminal to load the grades.json file:
mongoimport -d students -c grades < grades.json'''

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
		doc = grades.find({'type':'homework'}).sort([('student_id',pymongo.ASCENDING),('score',pymongo.ASCENDING)])

	except Exception as e:
		print "Unexpected Error: ", type(e), e

	student_id = None

	print "***** Deleting Minimum Score *****"
	for item in doc:
		try:
			if item['student_id'] != student_id:
				student_id = item['student_id']
				print "Student: %s -- Score: %s" % (student_id, item['score'])
				grades.remove({'_id': item['_id']})
		except Exception as e:
			print "Unexpected Error: ", type(e), e

	'''To verify that you have completed this task correctly, provide the identity 
	of the student with the highest average in the class with following query that 
	uses the aggregation framework.'''

	# "mongo shell:" - > db.grades.aggregate({'$group':{'_id':'$student_id','average':{'$avg':'$score'}}},{'$sort':{'average':-1}})

	# Answer = student_id = 54

def run():
	question_2()

if __name__ == "__main__":
	run()
