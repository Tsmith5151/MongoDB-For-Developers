## MongoDB University
<p align = "center">
<img src = "http://cdn.rancher.com/wp-content/uploads/2016/01/26001728/mongodb-logo.png">
</p>
#### C.R.U.D. Operations in Mongodb
The objective here is to go through the commands in the mongo shell to `Create`,`Read`,`Update` and `Delete` documents. 

#### Basic Commands to Access the Database:
  
- To create a new database, enter the mongo shell and type `use <db name>`. The database will not be created until the collection is added. To show the database has been created type `show dbs` and you will see the list of databases. If you want to view all of the collections inside the database -> `db.getCollectionNames()`. A note here, all documents must have a unique identifier (`_id`) within the collection. To drop this database -> `use <db name`> and then <`db.dropDatabase();`>. Lets look at importing a file into the database. For instance if we have a `JSON` file type, in the terminal type <`mongoimport -db <'db-name'> -collection <'collection-name'> --file <'file-name'>.JSON`>. Mongo includes a mongoexport utility which can dump a collection from a database: `mongoexport --db <database-name> --collection <collection-name> --out filename.json`

#### Create
- Two commands here we will look at, first is the `insert_one` and `insert_many` which creates a document in this collection and will create the collection if the collection does not already exist. So for example, if the database name is `videos`, you'll access this database by typing `use videos` and the collection name is `videos`
```
db.videos.insertOne({title:"Rocky",year:1968})
```
If done correctly, you can type `db.movies.find({})` and the movie should appear in the movies collection with the `_id`, `title`, and `year` of the movie. To print the output in JSON format, you can do this: `db.movies.find({}).pretty()`


