## MongoDB University
<p align = "center">
<img src = "http://cdn.rancher.com/wp-content/uploads/2016/01/26001728/mongodb-logo.png">
</p>
#### MongoDBFor Developers: M101P - Chapter 2 Homework
The objective of taking this course is to learn everything you need to know to get started building a MongoDB-based app. This course will go over basic installation, JSON, schema design, querying, insertion of data, indexing and working with the Python driver. We will also cover working in sharded and replicated environments. - Will be working with the `Pymongo` driver for the homeworks.  

#### Question 4.1

Given the collection with the following indexes:

```javascript
> db.products.getIndexes()
[
    {
        "v" : 1,
        "key" : {
            "_id" : 1
        },
        "ns" : "store.products",
        "name" : "_id_"
    },
    {
        "v" : 1,
        "key" : {
            "sku" : 1
        },
                "unique" : true,
        "ns" : "store.products",
        "name" : "sku_1"
    },
    {
        "v" : 1,
        "key" : {
            "price" : -1
        },
        "ns" : "store.products",
        "name" : "price_-1"
    },
    {
        "v" : 1,
        "key" : {
            "description" : 1
        },
        "ns" : "store.products",
        "name" : "description_1"
    },
    {
        "v" : 1,
        "key" : {
            "category" : 1,
            "brand" : 1
        },
        "ns" : "store.products",
        "name" : "category_1_brand_1"
    },
    {
        "v" : 1,
        "key" : {
            "reviews.author" : 1
        },
        "ns" : "store.products",
        "name" : "reviews.author_1"
    }
]
```
Which of the following queries can utilize at least one index to find all matching documents, or to sort? Check all that apply.

- (1) db.products.find( { 'brand' : "GE" } ).sort( { price : 1 } )
- (2) db.products.find( { $and : [ { price : { $gt : 30 } }, { price : { $lt : 50 } } ] } ).sort( { brand : 1 } )
- (3) db.products.find( { 'brand' : "GE" } )
- (4) db.products.find( { brand : 'GE' } ).sort( { category : 1, brand : -1 } )


#### Question 4.2
Suppose you have a collection called tweets whose documents contain information about the created_ at time of the tweet and the user's followers_count at the time they issued the tweet. What can you infer from the following explain output?

```javascript
> db.tweets.explain("executionStats").find( { "user.followers_count" : { $gt : 1000 } } ).limit(10).skip(5000).sort( { created_at : 1 } )
{
    "queryPlanner" : {
        "plannerVersion" : 1,
        "namespace" : "twitter.tweets",
        "indexFilterSet" : false,
        "parsedQuery" : {
            "user.followers_count" : {
                "$gt" : 1000
            }
        },
        "winningPlan" : {
            "stage" : "LIMIT",
            "limitAmount" : 0,
            "inputStage" : {
                "stage" : "SKIP",
                "skipAmount" : 0,
                "inputStage" : {
                    "stage" : "FETCH",
                    "filter" : {
                        "user.followers_count" : {
                            "$gt" : 1000
                        }
                    },
                    "inputStage" : {
                        "stage" : "IXSCAN",
                        "keyPattern" : {
                            "created_at" : -1
                        },
                        "indexName" : "created_at_-1",
                        "isMultiKey" : false,
                        "direction" : "backward",
                        "indexBounds" : {
                            "created_at" : [
                                "[MinKey, MaxKey]"
                            ]
                        }
                    }
                }
            }
        },
        "rejectedPlans" : [ ]
    },
    "executionStats" : {
        "executionSuccess" : true,
        "nReturned" : 10,
        "executionTimeMillis" : 563,
        "totalKeysExamined" : 251120,
        "totalDocsExamined" : 251120,
        "executionStages" : {
            "stage" : "LIMIT",
            "nReturned" : 10,
            "executionTimeMillisEstimate" : 500,
            "works" : 251121,
            "advanced" : 10,
            "needTime" : 251110,
            "needFetch" : 0,
            "saveState" : 1961,
            "restoreState" : 1961,
            "isEOF" : 1,
            "invalidates" : 0,
            "limitAmount" : 0,
            "inputStage" : {
                "stage" : "SKIP",
                "nReturned" : 10,
                "executionTimeMillisEstimate" : 500,
                "works" : 251120,
                "advanced" : 10,
                "needTime" : 251110,
                "needFetch" : 0,
                "saveState" : 1961,
                "restoreState" : 1961,
                "isEOF" : 0,
                "invalidates" : 0,
                "skipAmount" : 0,
                "inputStage" : {
                    "stage" : "FETCH",
                    "filter" : {
                        "user.followers_count" : {
                            "$gt" : 1000
                        }
                    },
                    "nReturned" : 5010,
                    "executionTimeMillisEstimate" : 490,
                    "works" : 251120,
                    "advanced" : 5010,
                    "needTime" : 246110,
                    "needFetch" : 0,
                    "saveState" : 1961,
                    "restoreState" : 1961,
                    "isEOF" : 0,
                    "invalidates" : 0,
                    "docsExamined" : 251120,
                    "alreadyHasObj" : 0,
                    "inputStage" : {
                        "stage" : "IXSCAN",
                        "nReturned" : 251120,
                        "executionTimeMillisEstimate" : 100,
                        "works" : 251120,
                        "advanced" : 251120,
                        "needTime" : 0,
                        "needFetch" : 0,
                        "saveState" : 1961,
                        "restoreState" : 1961,
                        "isEOF" : 0,
                        "invalidates" : 0,
                        "keyPattern" : {
                            "created_at" : -1
                        },
                        "indexName" : "created_at_-1",
                        "isMultiKey" : false,
                        "direction" : "backward",
                        "indexBounds" : {
                            "created_at" : [
                                "[MinKey, MaxKey]"
                            ]
                        },
                        "keysExamined" : 251120,
                        "dupsTested" : 0,
                        "dupsDropped" : 0,
                        "seenInvalidated" : 0,
                        "matchTested" : 0
                    }
                }
            }
        }
    },
    "serverInfo" : {
        "host" : "generic-name.local",
        "port" : 27017,
        "version" : "3.0.1",
        "gitVersion" : "534b5a3f9d10f00cd27737fbcd951032248b5952"
    },
    "ok" : 1
}
```
- (1) The query is a covered query.
- (2) The query uses an index to determine the order in which to return result documents.
- (3) The query examines 251120 documents.
- (4) The query uses an index to determine which documents match.
- (5) The query returns 251120 documents.

#### Question 4.3

There is a bug (TOOLS-939) affecting some versions of mongoimport and mongorestore that causes mongoimport `-d blog -c posts < posts.json` to fail. As a workaround, you can use mongoimport `-d blog -c posts < posts.json --batchSize 1`. Making the Blog fast Please download `hw4-3.zip` to get started. In this homework assignment you will be adding some indexes to the post collection to make the blog fast. We have provided the full code for the blog application and you don't need to make any changes, or even run the blog. But you can, for fun. We are also providing a patriotic (if you are an American) data set for the blog. There are 1000 entries with lots of comments and tags. You must load this dataset to complete the problem.

From the mongo shell:

```python 
use blog
db.posts.drop()
```
From the mac or PC terminal window: `mongoimport -d blog -c posts < posts.json` 

The blog has been enhanced so that it can also display the top 10 most recent posts by tag. There are hyperlinks from the post tags to the page that displays the 10 most recent blog entries for that tag. (run the blog and it will be obvious) The assignment is to make the following blog pages fast:

- The blog home page
- The page that displays blog posts by tag (http://localhost:8082/tag/whatever)
- The page that displays a blog entry by permalink (http://localhost:8082/post/permalink)
**Note:** By fast, we mean that indexes should be in place to satisfy these queries such that we only need to scan the number of documents we are going to return.

To figure out what queries you need to optimize, you can read the blog.py code and see what it does to display those pages. Isolate those queries and use explain to explore. Once you have added the indexes to make those pages fast run the following.

`python validate.py`

#### Question 4.4
In this problem you will analyze a profile log taken from a different mongoDB instance and you will import it into a collection named sysprofile. To start, please download sysprofile.json from Download Handout link and import it with the following command:

```mongoimport -d m101 -c profile < sysprofile.json```

Query the profile data, looking for all queries to the students collection in the database school2, sorted in order of decreasing latency. What is the latency of the longest running operation to the collection, in milliseconds?

- (1) 19776550
- (2) 10000000
- (3) 5580001
- (4) 15820
- (5) 2350
