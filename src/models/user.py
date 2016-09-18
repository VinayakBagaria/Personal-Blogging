import uuid
import datetime
from flask import session

from API.src.common.database import Database
from API.src.models.blog import Blog

class User(object):

    def __init__(self,email,password,_id=None):
        self.email=email
        self.password=password
        self._id=uuid.uuid4().hex if _id is None else _id

    @classmethod
    def get_by_id(cls,_id):
        data=Database.find_one(collection='users',query={'_id':_id})
        if data is not None:
            return cls(**data)

    @classmethod
    def get_by_email(cls,email):
        data=Database.find_one(collection='users',query={'email':email})
        if data is not None:
            return cls(**data)

    @staticmethod
    def login_valid(email,password):
        # Check if user email matches password
        user=User.get_by_email(email)
        if user is not None:
            # Check password
            return user.password==password
        return False

    @classmethod
    def register(cls,email,password):
        user=cls.get_by_email(email)
        if user is None:
            # user doesnot exist already
            new_user=cls(email,password)
            new_user.save_to_mongo()
            session['email']=email
            return True
        else:
            # User exists
            return False

    @staticmethod
    def login(user_email):
        # login_valid has already been called
        session['email']=user_email

    @staticmethod
    def logout():
        session['email']=None

    def get_blogs(self):
        # get blogs of a specific author
        return Blog.find_by_author_id(self._id)

    def json(self):
        return {
            'email':self.email,
            '_id':self._id,
            'password':self.password
        }

    def save_to_mongo(self):
        Database.insert('users',self.json())

    def new_blog(self,title, description):
        # author, title, description,author_id, _id=None
        blog=Blog(author=self.email,
                  title=title,
                  description=description,
                  author_id=self._id)
        blog.save_to_mongo()

    @staticmethod
    def new_post(blog_id,title,content,date=datetime.datetime.utcnow()):
        # title,content,date
        blog=Blog.from_mongo(blog_id)
        blog.new_post(title=title,
                      content=content,
                      date=date)