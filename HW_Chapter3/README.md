## MongoDB University
<p align = "center">
<img src = "http://cdn.rancher.com/wp-content/uploads/2016/01/26001728/mongodb-logo.png">
</p>
#### MongoDBFor Developers: M101P - Chapter 2 Homework
The objective of taking this course is to learn everything you need to know to get started building a MongoDB-based app. This course will go over basic installation, JSON, schema design, querying, insertion of data, indexing and working with the Python driver. We will also cover working in sharded and replicated environments. - Will be working with the `Pymongo` driver for the homeworks.  

#### Homework Questions:

##### Question 3.1:
Download the students.json file and import it into your local Mongo instance with this command:

```
mongoimport -d school -c students < students.json
```

Write a program in the language of your choice that will remove the lowest homework score for each student. Since there is a single document for each student containing an array of scores, you will need to update the scores array and remove the homework. Note: Remember, just remove a homework score. Don't remove a quiz or an exam! Remember with the new schema, this problem is a lot harder and that is sort of the point. One way is to find the lowest homework in code and then update the scores array with the low homework pruned. To verify that the program is correct, provide the identity (in the form of their _id) of the student with the highest average in the class with following query that uses the aggregation framework. The answer will appear in the _id field of the resulting document.


##### Question 3.2:
The question is centered on enhancing the blog project to insert entries into the posts collection. After this, the blog will work. It will allow you to add blog posts with a title, body and tags and have it be added to the posts collection properly.

As a reminder, to run your blog you type
```python blog.py```
To play with the blog you can navigate to the following URLs
- http://localhost:8082/
- http://localhost:8082/signup
- http://localhost:8082/login
- http://localhost:8082/newpost

You will be proving that it works by running our validation script as follows:
```python validate.py``
Once you get the blog posts working, validate.py will print out a validation code for HW 3.2.

##### Question 3.3:
Write a code to your blog so that it accepts comments using the same code from HW question 3.2. Once again, the area where you need to work is marked with an XXX in the blogPostDAO.py file. There is just one location that you need to modify. You don't need to figure out how to retrieve comments for this homework because the code you did in 3.2 already pulls the entire blog post.
 For the sake of clarity, here is a document out of the posts collection from a working project.

```javascript 
{
    "_id" : ObjectId("509df76fbcf1bf5b27b4a23e"),
    "author" : "erlichson",
    "body" : "This is a blog entry",
    "comments" : [
        {
            "body" : "This is my comment",
            "author" : "Andrew Erlichson"
        },
        {
            "body" : "Give me liberty or give me death.",
            "author" : "Patrick Henry"
        }
    ],
    "date" : ISODate("2012-11-10T06:42:55.733Z"),
    "permalink" : "This_is_a_blog_post_title",
    "tags" : [
        "cycling",
        "running",
        "swimming"
    ],
    "title" : "This is a blog post title"
}
```
Note that you add comments in this blog from the blog post detail page, which appears at `http://localhost:8082/post/post_slug` where `post_slug` is the permalink. For the sake of eliminating doubt, the permalink for the example blog post above is `http://localhost:8082/post/This_is_a_blog_post_title`. Run validation.py to check your work, much like the last problem. Validation.py will run through and check the requirements of HW 3.2 and then will check to make sure it can add blog comments, as required by this problem, HW 3.3. It checks the web output as well as the database documents.
