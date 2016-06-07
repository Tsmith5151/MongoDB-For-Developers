import pymongo
import sys
import datetime


try:
	connection = pymongo.MongoClient("mongodb://localhost")
except Exception as e:
	print "Unexpected error: ", type(e), e

def find_modify():
	print "hello"

def run():
	find_modify()

if __name__=="__main__":
	run()