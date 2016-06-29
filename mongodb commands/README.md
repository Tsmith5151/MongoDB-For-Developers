## MongoDB University
<p align = "center">
<img src = "http://cdn.rancher.com/wp-content/uploads/2016/01/26001728/mongodb-logo.png">
</p>
#### C.R.U.D. Operations in Mongodb
- The objective here is to go through the commands in the mongo shell to `Create`,`Read`,`Update` and `Delete` documents. The MongoDB documents can be found [`here`](https://docs.mongodb.com).

#### Basic Commands to Access the Database:
  
- To create a new database, enter the mongo shell and type `use <db name>`. The database will not be created until the collection is added. To show the database has been created type `show dbs` and you will see the list of databases. If you want to view all of the collections inside the database -> `db.getCollectionNames()`. A note here, all documents must have a unique identifier (`_id`) within the collection. To drop this database -> `use <db name`> and then <`db.dropDatabase();`>. Lets look at importing a file into the database. For instance if we have a `JSON` file type, in the terminal type <`mongoimport -db <'db-name'> -collection <'collection-name'> --file <'file-name'>.JSON`>. Mongo includes a mongoexport utility which can dump a collection from a database: `mongoexport --db <database-name> --collection <collection-name> --out filename.json`

#### Create
- The two principle commands for creating documents we will look at is the `insertOne` and `insertMany` which creates a document in a collection and will create the collection if the collection does not already exist. So for example, if the database name is `videos`, you'll access this database by typing `use videos` and the collection name is `videos`

```python
#Query
db.videos.insertOne({title:"Rocky",year:1968})
```

- If done correctly, you can type `db.movies.find({})` and the movie should appear in the movies collection with the `_id`, `title`, and `year` of the movie. To print the output in JSON format, you can do this: `db.movies.find({}).pretty()`. As mentioned earlier, that when inserting a document into a collection, the document must contain a `_id`. If one is not provided, mongodb will create a random unique id for the document or you can provide a custom identification by specifying the id value, for example : `_id:tt59448289`. You want to make sure also that if you have a custom id that all of the id's have the same form. Shown below is an example if you want to insert a batch of documents into the collection, you would use the `insertMany` command. Instead of passing a single document as the first argument, we pass an arrary of n-elements (each element is a separate document). Each document in the array will have a object ID assigned to them as well, if not specified.

```python 
#insertMany:
db.movies.insertMany([{
                      title:"Star Trek II. The Wrath of Khan",
                      year: 1982,
                      type: "movie
                      },
                      {title: "Star Trek"
                      year: 2009
                      type:"movie"}])
```
- A note here is that by default insertMany does an ordered insert, meaning that as soon as an error is encountered, it will stop inserting documents. An example of this is if you are customizing the `_id` value, you may have an instance where duplicate documents exists. But we may want keep going and insert the rest of the documents even though an error was raised. Adding a second argument `ordered:false` to the insertMany command, meaning that mongodb will run an unordered insertMany command - if an error is encountered, it will keep inserting the remaining documents. 

```python
#insert many:
db.movies.insertMany([{
                      title:"Star Trek II. The Wrath of Khan",
                      year: 1982,
                      type: "movie,
                      rated: "PG-13"
                      },
                      {title: "Star Trek"
                      year: 2009
                      type:"movie",
                      rated:"PG-13"}],ordered: false)
```
- If you wanted to count the multiple documents that were uploaded in the collections, simply type: `db.movies.find({}).count(). Another example, say we wanted to find all the movies in 2003, and rated PG-13. The query would look like this:

 ```python
 db.movies.find({year:2013,rated:"PG-13"}).pretty()
 ```

- Expanding upon the `_id`, MongoDB creates unique ID if not specified by default as an ObjectID, this is a value type defined in the BSON spec and is structured as 12-byte-hex string: ``` _ _"A" _ _ | _ "B"_ _ | _"C" _ | _"D" _ _ ``` Note: description of the "A", "B", "C", and "D" blocks don't actually appear in the `_id` value, but for the sake of explaining the blocks, the letter are used as references
  - A: Timestamp (4)
  - B: Address where the MongoDB server is running - Machine Identifier (3)
  - C: Process ID (2)
  - D: Counter; random number generator (3)
  - Total 12 bytes

#### Reading
- In the previous section, we looked at basic queries for scalar fields, here we will match for equality against embedded documents, arrays, and other nested structures. Shown below is an example where a nested array is now part of the document. The goal here is now is to do an equality match for the documents that has a tomator meter of 99.

```python
    "tomato" : {
        "meter" : 99,
        "image" : "certified",
        "rating" : 8.9,
        "reviews" : 287,
        "fresh" : 283,
        "consensus" : "Deftly blending comedy, adventure, and honest emotion, Toy Story 3 is a rare second sequel that really works.",
        "userMeter" : 89,
        "userRating" : 4.3,
        "userReviews" : 602138
    },
```
- Note the tomato field stores a nested document with a number of fields (i.e. meter) - the keys must be enclosed in quotes using the dot notation. To sum up, to drive down the hierarchy of nested documents, you reach into documents at each additional level of nesting by strining field names together using dot notation as shown below. 

```python
db.moves.find({"tomato.meter":99}).pretty()
```

###### Eqaulity matches on Arrarys:
- On the entire arrary
- Based on any element
- Based on a specific element (say matching only arrarys who's first element matches specific criteria)

- The example here is to identify documents with exact matches to an array of one or more values. Again, the document now contains an array field of writers in the document.

```python 
    "writers" : [
        "John Lasseter",
        "Andrew Stanton",
    ]
```
- Keep in mind that order 0f the elements matters and that only the documents with the specified order in the array will be returned. The query will look like this:

```python
db.movies.find({writers: ["John Lasseter", "Andrew Stanton"]})
```

- Note: If you don't want an exact match, then you wouldn't enclose the value you are looking for in brackets. Here if you wanted to return all the documents that contain John Lasseter in the writers array you would do this:

```python
db.movies.find({writers: "John Lasseter"})
```

- This example we will look at matching array elements occurring in a specific position in an array. Adding on to the previous document, we now have a field with an array of actors. The first entry is typically the main actor, so we want to find all of the movies where Tom Hanks is the main actor (i.e. first element in the array):

```python
    "actors" : [
        "Tom Hanks",
        "Tim Allen",
        "Joan Cusack",
        "Ned Beatty"
    ]
```
 ```python
 #Query: First actor in array list
 db.movies.find({actors.1:"Tom Hanks"})
 ```

###### Cursors and Projection:
- Cursors: the find method returns cursors and to access these documents you need to iterate through the cursors. In the Mongo shell, if we don't assign the return value from "find" to a variable using the keyword `var` the cursor is automatically iterated up to 20 times to print an initial set of search results. In general, the MongoDB server returns the query results in batches; the batch size will not exceed the maximum BSON document size and for most queries. For most queries, the first batch returns 101 documents or just enouch documents to exceed 1 MB. (note: it is possible to override the default batch size). So as we iterate through the cursor and reach the end of the return batch, if there is more results `cursor.next` will perform a get more operation to retrieve the next batch. Typing `it` in the command line will iterate through the batches. If you want to see how many documents are remaining in the batch, first you will need to assign the query to a variable: `var c = db.movies.find({});` then  `c.objectLetInBatch()`.

- Projection: handy way of reducing the size of the returned for any one query. By default, MongoDB returns all fields in all matching documents for queries. Projections reduce network overhead and processing requirements by limiting the fields returned in the document. 
Example, if we wanted to just return the all of the movie titles:

```python
# Return only the docs showing the title name:
db.movies.find({},{title:1}) 
```

```python 
#`_id` is always returned by default. We can exclude this by the following:
db.movies.find({},{title:1, _id, 0})
```

###### Query Operators:
- Comparison Operators: match on the basis of a field's value relative to some other value. In this example, a scalar field `runtime` is added to the doucment. In the mongo shell, you can use operators such as $eq, $gte, $gt, $lte, $lt, $in, $ne (search the mongo docs for a complete list of comparison operators). When using these operators, you are not limited to just a single field. 

```
#Query for runtime greater than or equal to 100 and less than 130 minutes
db.movies.find({'tomato.meter': 95, runtime: {$gte: 100, $lt: 130}},{title:1, _id:0}).pretty()
```

```
#Find all movies that have ratings ($ne = not equal to)
db.movies.find({rating, {$ne : "UNRATED"}}).pretty()
```
- Typically in MongoDB data models, rather than store a null value for a field, we will simply not store that field at all. 

```
#Query: Give me all the movies that have a rating of PG or PG-13 ($in must be an array)
db.movies.find({rating : {$in : ["PG", PG-13"]}}).pretty()
```

###### Element Operators:
- Element operators have to do with the shape of the documents, meaning this allows us to detect the presence of absence of a given field. The two operators examined here are:
  - $ exist: matches documents that have the same specified field
  - $ type: selects documents if a field is of the specified type

```
#Example here is to find all the documents with a tomator.meter field (can change to false - shows movies that do not contain this field:
db.movies.find({'tomator.meter':{$exists: true}})
```

```
#Count the number movies that have an _id value that is a string (this would be if you customized the _id such as _id: "ABCD"
db.movies.find({_id:{$type:string}}).count()
```
###### Logical Operators:
- $or : joins query clauses with a logical OR returns all documents that match the conditions of either clause
- $and : joins query clauses with a logical AND returns all documents that match the conditions of either clause
- $not : Inverts the effect of a query expression and returns documents that do not mach the query expression
- $nor: Joins query clauses with a logical NOR returns all documents that fail to match both clauses

- In this example, `metacritic` scalar field is added to the documents; this is another source that provides movie ratings

```
#Find all movies with rating from either source that satisfies the following comparison operators
db.moves.find({$or:{'tomato.meter':{$gte:95}},{metacritc:{$gte:90}}}).pretty()
```

```
#Find all movies with rating from both source that satisfies the following comparison operators
db.moves.find({and:{'tomato.meter':{$gte:95}},{metacritc:{$gte:90}}}).pretty()
```
- Note when using the and operator, the query above is equivalent to the query shown below. The reason is that criteria specified for this query document are implicitly $anded together. 

```
#Find all movies with rating from both source that satisfies the following comparison operators
db.moves.find({'tomato.meter':{$gte:95},metacritc:{$gte:90}}).pretty()
```

```
#An example where you would want to use the "and" logical query operator
db.moves.find({$and:[{metacritic:{$ne: null}},{metacritic"{$exists:true}}]}).pretty()
```
###### Regular Expressions:
- Using regular expressions allows us to match fields with string values. For this example, I've added awards field that contains a subdocument with a text subfield. Also, take note that the "text" subfield is structured such that if a movie won a Oscar, then the first word would say "Won". If the movie did not win an Oscar but nominated for one, the first word of the string will simply say "Nominated". The goal of this query would be to return all of the movies that won an Oscar. 

```python
    "awards" : {
        "oscars" : [
            {"bestAnimatedFeature": "won"},
            {"bestMusic": "won"},
            {"bestPicture": "nominated"},
            {"bestSoundEditing": "nominated"},
            {"bestScreenplay": "nominated"}
        ],
        "wins" : 56,
        "nominations" : 86,
        "text" : "Won 2 Oscars. Another 56 wins & 86 nominations."
    }
  ```
```
#An example where you would want to use the "and" logical query operator
db.moves.find({"awards.text":{$regex: /^Won\s.*/}}).pretty()
```
- Note, the // delimit the regular expression, the ^ means start at the beginning of whatever value we're matching against and match exactly a capital W, lowercase o, lowercase n. The * means to match any character any number of times and \s is the space character. So basically what this query is saying is give me all documents where the awards.text field begins with the word Won. 

###### Array Operators:
- $all : matches arrays that contain ALL elements specified in the query 
- $elemMatch : selects documents if element in the array field matches all the specified $elemMatch conditions
- $size : selects documents if the array field is a specified size

- In this example, the genres is added to the documents in the movies collection to illustrate using array operators.

```python
    "genres" : [
        "Animation",
        "Adventure",
        "Comedy"
    ],
```

```
#Return all movies with the genres Comedy, Crime, and Data
db.moves.find({genres: {$all: ["Comedy","Crime","Data"]}}).pretty()
```

``` 
#Using $size to match all documents based on the length of an array
#Query: find all movies filmed in the country of origin (i.e. filmed in one country)
db.moves.find({countries: {$size: 1}}).pretty()
```
- Now lets add in the following array with embedded documents:

```python
boxOffice :[{"country":"United States", "revenue": 19.5},
            {"country":"United Kingdom", "revenue": 22.5}]
```
```
#Using $elemMatch to find all of the movies filmed in the U.S. with a revenue greater than 15 million
#Note elemMatch is used when you have an array with embedded documents shown above.
db.moves.find({boxOffice: {$elemMatch: { country: "USA", revenue: {$gte:15}}}}).pretty()
```
- The above query, elemMatch requires that all criteria be satisfied within a single element of an array field (i.e. both criteria should be met within a single element of the box office).


###### Aggregation:
- Aggregation pipeline operations have a collection of operators available to define and manipulate documents in pipeline stages. [documents](https://docs.mongodb.com/manual/reference/operator/aggregation-pipeline/) such as `Projects` (reshapes the documents), `unmatch` (filtering step), and `sort`(sorts documents in a particular order). Also, aggregation is `unwind`, which deconstructs an array field from the input documents to output a document for each element. Each output document is the input document with the value of the array field replaced by the element. So for instance, if we had an array of tags = ["blue","red","white"] and we "unwind" the tags, then we will have three different documents now (expands 1:n) --> tags:blue, tags:red, tags:white. 

*$Group*
- The complete dataset for this example can be found in the Dataset directory under the filename `population.json`. Below shows a snipets of a document located in the `zips` collection. Keep in mind there are several aggregation expressions in the group stage such as $sum, $avg, $min, $max, $push, $addToSet, $first, $last. The following section walks through several queries using the aggregation group expressions in the Mongo shell. 

```javascript
{
    "city" : "CLANTON",
    "loc" : [
        -86.642472,
        32.835532
    ],
    "pop" : 13990,
    "state" : "AL",
    "_id" : "35045"
}
```

- Write an aggregation expression to calculate the total population of a zip code (postal code) by state. As before, the postal code is in  the `_id` field and is unique. 

```javascript
db.zips.aggregate([
	{'$group':
		{_id:'$state',
		'population':{$sum:'$pop'}
		}
	}
])
```
- Write an aggregation expression to calculate the average population of a zip code (postal code) by state. As before, the postal code is in  the `_id` field and is unique. 

```javascript
db.zips.aggregate([
	'$group':
		{_id:{
			'state':'$state'
			},
		'population':{$avg:'$pop'}
	}
])
```

- Write an aggregation query that will return the postal codes that cover each city.

```javascript
db.zips.aggregate([
	{'$group':
		{_id:{
			'city':'$city'
			},
		'zip_codes':{$addToSet:'$_id'}
		}
	}
])
```

- Write an aggregation query that will return the population of the postal code in each state with the highest population.

```javascript
db.zips.aggregate([
	{'$group':
		{_id:{
			'state':'$state'
			},
		'max_population':{$max:'$pop'}
		}
	}
])
```
