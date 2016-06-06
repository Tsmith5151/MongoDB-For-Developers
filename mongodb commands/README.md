## MongoDB University
<p align = "center">
<img src = "http://cdn.rancher.com/wp-content/uploads/2016/01/26001728/mongodb-logo.png">
</p>
#### C.R.U.D. Operations in Mongodb
The objective here is to go through the commands in the mongo shell to `Create`,`Read`,`Update` and `Delete` documents. 

#### Basic Commands to Access the Database:
  
- To create a new database, enter the mongo shell and type `use <db name>`. The database will not be created until the collection is added. To show the database has been created type `show dbs` and you will see the list of databases. If you want to view all of the collections inside the database -> `db.getCollectionNames()`. A note here, all documents must have a unique identifier (`_id`) within the collection. To drop this database -> `use <db name`> and then <`db.dropDatabase();`>. Lets look at importing a file into the database. For instance if we have a `JSON` file type, in the terminal type <`mongoimport -db <'db-name'> -collection <'collection-name'> --file <'file-name'>.JSON`>. Mongo includes a mongoexport utility which can dump a collection from a database: `mongoexport --db <database-name> --collection <collection-name> --out filename.json`

#### Create
- Two commands here we will look at, first is the `insertOne` and `insertMany` which creates a document in this collection and will create the collection if the collection does not already exist. So for example, if the database name is `videos`, you'll access this database by typing `use videos` and the collection name is `videos`
```
db.videos.insertOne({title:"Rocky",year:1968})
```
If done correctly, you can type `db.movies.find({})` and the movie should appear in the movies collection with the `_id`, `title`, and `year` of the movie. To print the output in JSON format, you can do this: `db.movies.find({}).pretty()`. As mentioned earlier, that when inserting a document into a collection, the document must contain a `_id`. If one is not provided, mongodb will create a random unique id for the document or you can provide a custom identification by specifying the id value, for example : `_id:tt59448289`. You want to make sure also that if you have a custom id that all of the id's have the same form. Shown below is an example if you want to insert a batch of documents into the collection, you would use the `insertMany` command. Instead of passing a single document as the first argument, we pass an arrary of n-elements (each element is a separate document). Each document in the array will have a object ID assigned to them as well, if not specified.

```
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
A note here is that by default insertMany does an ordered insert, meaning that as soon as an error is encountered, it will stop inserting documents. An example of this is if you are customizing the `_id` value, you may have an instance where duplicate documents exists. But we may want keep going and insert the rest of the documents even though an error was raised. Adding a second argument `ordered:false` to the insertMany command, meaning that mongodb will run an unordered insertMany command - if an error is encountered, it will keep inserting the remaining documents. 

#insert many:
db.movies.insertMany([{
                      title:"Star Trek II. The Wrath of Khan",
                      year: 1982,
                      type: "movie
                      },
                      {title: "Star Trek"
                      year: 2009
                      type:"movie"}],ordered: false)
