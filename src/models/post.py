import datetime
import uuid

from API.src.common.database import Database


class Post(object):

    def __init__(self, blog_id, title, content, author, created_date=datetime.datetime.utcnow(),_id=None):
        self.blog_id=blog_id
        self.title=title
        self.content=content
        self.author=author
        self.created_date=created_date
        # to generate an unique id in hex format 32 char
        self._id=uuid.uuid4().hex if _id is None else _id

    def save_to_mongo(self):
        Database.insert(collection='posts',data=self.json())

    # Create a json representation of the post itself via set to store in mongo db
    def json(self):
        return {
            '_id':self._id,
            'blog_id':self.blog_id,
            'author':self.author,
            'content':self.content,
            'title':self.title,
            'created_date':self.created_date
        }

    # search a blog acccording to a id
    @classmethod
    def from_mongo(cls, _id):
        post_data= Database.find_one(collection='posts', query={'_id':_id})
        return cls(**post_data)
        """ **post_data work :
                blog_id=post_data['blog_id'],
                   title=post_data['title'],
                   content=post_data['content'],
                   author=post_data['author'],
                   created_date=post_data['created_date'],
                   _id=post_data['_id']
        """
    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection='posts',query={'blog_id':id})]