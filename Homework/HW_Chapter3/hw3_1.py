#mongoimport -d school -c students < students.json

from pymongo import MongoClient
from sys import exc_info

#Drops the lowest Homework score for each student in the collection:

def lowest_hw(scores):
	lowest = None
	lowest_score = 101
	for i in scores:
		if((i)['type'] == "homework" and (i['score'] < lowest_score)):
			#found a new bound
			lowest = i
			lowest_score = lowest['score']
	return lowest

def remove_lowest(collection):
	cursor = collection.find()
	for student in cursor:
		_id = student["_id"]
		print "Looking at student {_id}:".format(_id=_id)
		scores = student['scores']
		lowest = lowest_hw(scores)
		if(lowest is not None):
			print(" Removing hw grade of {score}").format(score=lowest['score'])
			scores.remove(lowest)
			collection.update_one({'_id':_id},
								{'$set':{'scores':scores}})
		else:
			print "Could not find a homework score to process"

def main():
	'''Establishes a client and drops the lowest HW score for each student'''
	host = 'localhost'
	port = 27017
	dbname = 'school'
	coll_name = 'students'

	client = MongoClient(host=host,port=port)
	db = client[dbname]
	collection = db[coll_name]

	print ("Removing lowest score from students in the {db}.{collection} "
           "namespace."
           ).format(db=db.name, collection=collection.name)
	remove_lowest(collection=collection)

if __name__ == "__main__":
	main()