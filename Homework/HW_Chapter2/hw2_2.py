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

#First task is to find which student has the highest average in the class
db = connection.students
grades = db.grades

def remove_score(_id):
	db = connection.students
	grades = db.grades
	try: 
		doc = grades.find_one({'_id':_id})
		print "Removing score ", doc['score'], "for student ", doc['student_id']
		grades.remove({'_id':'id'})
	except Exception as e:
		print "Unexpected Error: ", type(e), e

def remove_lowest():	
	try:
		doc = grades.find({'type':'homework'}).sort([('student_id',pymongo.ASCENDING),('score',pymongo.ASCENDING)])

	except Exception as e:
		print "Unexpected Error: ", type(e), e

	student_id = -1

	print "***** Deleting Minimum Score *****"
	for item in doc:
		try:
			if item['student_id'] != student_id: #it's a new id
				remove_score(item['_id'])
			student_id = item['student_id'] #updates student id
		except Exception as e:
			print "Unexpected Error: ", type(e), e

	'''To verify that you have completed this task correctly, provide the identity 
	of the student with the highest average in the class with following query that 
	uses the aggregation framework.'''

	# "mongo shell:" - > db.students.aggregate({'$unwind':'$scores'},{'$group':{'_id':'$_id', 'average':{$avg:'$scores.score'}}}, {'$sort':{'average':-1}}, {'$limit':1})

	# Answer = student_id = 54

def run():
	remove_lowest()

if __name__ == "__main__":
	run()
