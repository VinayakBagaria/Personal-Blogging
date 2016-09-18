from API.src.models.user import User
from flask import Flask, render_template, request, session, make_response
from API.src.common.database import Database
from API.src.models.blog import Blog
from API.src.models.post import Post

app=Flask(__name__)
app.secret_key="jose"

@app.route('/auth/login',methods=['POST'])
def login_user():
    email=request.form['email']
    password=request.form['password']

    if User.login_valid(email,password):
        User.login(email)
        return render_template('profile.html',email=session['email'])
    else:
        return render_template('register.html',variable=1)



@app.route('/auth/register',methods=['POST'])
def register_user():
    email=request.form['email']
    password=request.form['password']
    User.register(email,password)
    return render_template('profile.html',email=session['email'])

@app.route('/login')
def login_template():
        return render_template('login.html')

@app.route('/register')
def register_template():
        return render_template('register.html',variable=0)

#Find blogs by id
@app.route('/blogs/<string:user_id>')
@app.route('/blogs')
def user_blogs(user_id=None):
    if user_id is not None:
        user=User.get_by_id(user_id)
    else:
        user=User.get_by_email(session['email'])

    blogs=user.get_blogs()

    return render_template('user_blogs.html',blogs=blogs,email=user.email)

@app.route('/blogs/new',methods=['POST','GET'])
def create_new_blog():
    """
    If GET, user just arrived here
    If POST, user submitted whatever he wants new to write
    """
    if request.method=="GET":
        return render_template("new_blog.html")
    else:
        title=request.form['title']
        description=request.form['description']
        user=User.get_by_email(session['email'])

        new_blog=Blog(user.email,title,description,user._id)
        new_blog.save_to_mongo()

        return make_response(user_blogs(user._id))

@app.route('/posts/<string:blog_id>')
def blog_posts(blog_id):
    blog=Blog.from_mongo(blog_id)
    posts=blog.get_posts()

    return render_template('posts.html',posts=posts,blog_title=blog.title,blog_id=blog_id)

@app.route('/posts/new/<string:blog_id>',methods=['POST','GET'])
def create_new_post(blog_id):
    """
    If GET, user just arrived here
    If POST, user submitted whatever he wants new to write
    """
    if request.method=="GET":
        return render_template("new_post.html",blog_id=blog_id)
    else:
        title=request.form['title']
        content=request.form['content']
        user=User.get_by_email(session['email'])

        new_post=Post(blog_id, title, content, user.email)
        new_post.save_to_mongo()

        return make_response(blog_posts(blog_id))

@app.route('/')
def home_template():
    return render_template('login.html')

@app.before_first_request
def initialise_database():
    Database.initalise()

if __name__=="__main__":
    app.run(port=4587,debug=False)
