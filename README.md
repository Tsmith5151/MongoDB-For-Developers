## MongoDB University
<p align = "center">
<img src = "http://cdn.rancher.com/wp-content/uploads/2016/01/26001728/mongodb-logo.png">
</p>
#### MongoDBFor Developers: M101P - Chapter 2 Homework
The objective of taking this course is to learn everything you need to know to get started building a MongoDB-based app. This course will go over basic installation, JSON, schema design, querying, insertion of data, indexing and working with the Python driver. We will also cover working in sharded and replicated environments. - Will be working with the `Pymongo` driver for the homeworks.  

#### Homework Questions:

##### Question 2.1:
In this problem, you will be using a collection of student scores that is similar to what we used in the lessons. Please download grades.json from the Download Handout link and import it into your local mongo database as follows: ```mongoimport -d students -c grades < grades.json```. The dataset contains 4 scores for 200 students. First, let's confirm your data is intact; the number of documents should be 800. This next query, which uses the aggregation framework that we have not taught yet, will tell you the student_id with the highest average score:

``` 
db.grades.aggregate({'$group':{'_id':'$student_id', 'average':{'$avg':'$score'}}}, {'$sort':{'average':-1}}, {'$limit':1})
```
The answer should be 'student_id' 164 with an average of approximately 89.3. Now it's your turn to analyze the data set. Find all exam scores greater than or equal to 65, and sort those scores from lowest to highest. What is the student_id of the lowest exam score above 65? 

##### Question 2.2:
Write a program in the language of your choice that will remove the grade of type "homework" with the lowest score for each student from the dataset in the handout. Since each document is one grade, it should remove one document per student. This will use the same data set as the last problem, but if you don't have it, you can download and re-import.The dataset contains 4 scores each for 200 students. First, let's confirm your data is intact; the number of documents should be 800.

``` db.grades.count() ```

Hint/spoiler: If you select homework grade-documents, sort by student and then by score, you can iterate through and find the lowest score for each student by noticing a change in student id. As you notice that change of student_id, remove the document. To confirm you are on the right track, here are some queries to run after you process the data and put it into the grades collection:

Let us count the number of grades we have: the number of documents should be 800. ``` db.grades.count() ```
The result should be 600. Now let us find the student who holds the 101st best grade across all grades:
``` db.grades.find().sort( { 'score' : -1 } ).skip( 100 ).limit( 1 ) ```
The correct result will be:
```
{ "_id" : ObjectId("50906d7fa3c412bb040eb709"), "student_id" : 100, "type" : "homework", "score" : 88.50425479139126 }
```
Now let us sort the students by student_id, type, and score, and then see what the top five docs are:
```
db.grades.find({},{'student_id':1,'type':1,'score':1,'_id':0}).sort({'student_id':1,'score': 1}).limit(5)
```
The result set should be:
```
{ "student_id" : 0, "type" : "quiz", "score" : 31.95004496742112 }
{ "student_id" : 0, "type" : "exam", "score" : 54.6535436362647 }
{ "student_id" : 0, "type" : "homework", "score" : 63.98402553675503 }
{ "student_id" : 1, "type" : "homework", "score" : 44.31667452616328 }
{ "student_id" : 1, "type" : "exam", "score" : 74.20010837299897 }
```
To verify that you have completed this task correctly, provide the identity of the student with the highest average in the class with following query that uses the aggregation framework. The answer will appear in the _id field of the resulting document.
```
db.grades.aggregate({'$group':{'_id':'$student_id','average':{$avg:'$score'}}},{'$sort':{'average':-1}},{'$limit':1})
```
##### Question 2.3:
In the blog directory, you will see three files at the highest level: blog.py, userDAO.py and sessionDAO.py. There is also a views directory which contains the templates for the project. The project roughly follows the model/view/controller paradigm. userDAO and sessionDAO.py comprise the model. blog.py is the controller. The templates comprise the view. If everything is working properly, you should be able to start the blog by typing: ``` python blog.py ```. If you go to http://localhost:8082 you should see a message, "this is a placeholder for the blog". Here are some URLs that must work when you are done.

```
http://localhost:8082/signup
http://localhost:8082/login
http://localhost:8082/logout
```
When you login or sign-up, the blog will redirect to http://localhost:8082/welcome and that must work properly, welcoming the user by username. We have removed two pymongo statements from userDAO.py and marked the area where you need to work with XXX. You should not need to touch any other code. The pymongo statements that you are going to add will add a new user to the database upon sign-up, and validate a login by retrieving the right user document. The blog stores its data in the blog database in two collections, users and sessions. Once you have the the project working, the following steps should work:

- go to http://localhost:8082/signup
- Create a user
- It should redirect you to the welcome page and say: welcome username, where username is the user you signed up with. Now
- Go to http://localhost:8082/logout
- Now login http://localhost:8082/login.

##### Question 2.4:
Access the `hw2_3_drump` directory. Which of the choices below is the title of a movie from the year 2013 that is rated PG-13 and won no awards? Query the video.movieDetails collection to find the answer.

There is a dump of the video database included in the handouts for the "Creating Documents" lesson. Use that data set to answer this question. Loading in the dump file to Mongodb: in the terminal type: mongorestore --drop -d movies -c movieDetails movieDetails.bson

##### Question 2.5:
Continuing from Question 2.4, how many movies list "Sweden" second in the the list of countries?
