#Scrape the data from the reddit homepage as JSON file and then import into MongoDB
import pymongo
import urllib2
import json

try:
	# Connect to the database
	connection = pymongo.MongoClient("mongodb://localhost")
	# Get a handle to the reddit database
	db = connection.reddit
	stories = db.stories
	#drop exisiting database
	#stories.drop()

except Exception as e:
	print "Unsuccessful attempt to connect to database", type(e),e

def get_data():
	# reddit API requires a user agent to be specified:
	hdr={ 'User-Agent': 'Using for my M101P: Mongo for Developers course'}
	req = urllib2.Request("http://www.reddit.com/r/technology/.json", headers=hdr)
	
	# get the reddit home page
	reddit_page = urllib2.urlopen(req)

	# parse the json into python objects
	parsed = json.loads(reddit_page.read())
	
	#iterate through each news item on the page:
	for item in parsed['data']['children']:
		#put in the mongo database:
		stories.insert_one(item['data'])

def search_title():
	#Query database for title containing "apple & google"
	query = {'title':{'$regex': 'technology', '$options': 'i'}} # i = case insensitivity to match upper and lower cases
	projection = {'title': 1,'_id': 0}

	try:
		cursor = stories.find(query,projection)

	except Exception as e:
		print "Unexpected error:", type(e), e

	for doc in cursor:
		print doc 

def run():
	#get_data()
	search_title()

if __name__=="__main__":
	run()
