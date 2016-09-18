# Personal-Blogging API using MongoDB,HTML,Flask and Python

The project uses Flask which is a framework for Python based on Werkzeug, Jinja 2. I use Jinja 2 for the HTML page.
It also uses MongoDB for database design.

<h1>Run app.py file in your python editor and then follow the link</h1>
![alt tag](https://github.com/VinayakBagaria/Personal-Blogging/blob/master/run_app.JPG)

<h3>FEATURES : </h3>
  Login Page for old users
  <br>
  ![alt tag](https://github.com/VinayakBagaria/Personal-Blogging/blob/master/login.JPG)
  Register Page for new users
  <br>
  New Blogs Option
  <br>
  ![alt tag](https://github.com/VinayakBagaria/Personal-Blogging/blob/master/blogs.JPG)
  New posts under each blog
  <br>
  ![alt tag](https://github.com/VinayakBagaria/Personal-Blogging/blob/master/post.JPG)
  
1. src/common/database refers to the operations with mongodb. Don't forget to start the mongo db server before executing the python code.
2. src/models/blog is the file which describes a blog and saves it to our database.
3. src/models/post is the file which helps us to create a new post in a blog.
4. src/models/user registers/logins a user.

src/templates contain the HTML files with Jinja variables used in it. I have used Bootstrap to give some designing.

<p align="center">
  <img src="C:\Users\bagariavinayak\Pictures\login.jpg" width="350"/>
</p>


