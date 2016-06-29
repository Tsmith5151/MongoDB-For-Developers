from pymongo import MongoClient
from sys import exc_info

#Aggregation Examples:

def example1(collection):
	db.collection..aggregate([
		{$group:
			{_id:'$manufacturer',
			{num_products:{$sum:1}}
			}
		}
		])

def main():
	'''Establishes a client and drops the lowest HW score for each student'''
	host = 'localhost'
	port = 27017
	dbname = 'inventory'
	coll_name = 'products'

	client = MongoClient(host=host,port=port)
	db = client[dbname]
	collection = db[coll_name]


if __name__ == "__main__":
	main()