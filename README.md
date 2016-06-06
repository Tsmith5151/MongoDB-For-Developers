## MongoDB University
<p align = "center">
<img src = "http://cdn.rancher.com/wp-content/uploads/2016/01/26001728/mongodb-logo.png">
</p>
#### MongoDBFor Developers: M101P - Chapter 2 Homework
- The objective of taking this course is to learn everything you need to know to get started building a MongoDB-based app. This course will go over basic installation, JSON, schema design, querying, insertion of data, indexing and working with the Python driver. We will also cover working in sharded and replicated environments. - Will be working with the `Pymongo` driver for the homeworks.  

#### Homework Questions:

- 2.1: In this problem, you will be using a collection of student scores that is similar to what we used in the lessons. Please download grades.json from the Download Handout link and import it into your local mongo database as follows:

```mongoimport -d students -c grades < grades.json```

The dataset contains 4 scores for 200 students. First, let's confirm your data is intact; the number of documents should be 800.

``usestudentsdb.grades.count()`` - You should get 800.

This next query, which uses the aggregation framework that we have not taught yet, will tell you the student_id with the highest average score:

``` python
db.grades.aggregate({'$group':{'_id':'$student_id', 'average':{$avg:'$score'}}}, {'$sort':{'average':-1}}, {'$limit':1})
```

The answer should be student_id 164 with an average of approximately 89.3. Now it's your turn to analyze the data set. Find all exam scores greater than or equal to 65, and sort those scores from lowest to highest. What is the student_id of the lowest exam score above 65? 
