import datetime
import uuid

from API.src.models.post import Post
from API.src.common.database import Database


class Blog(object):
    def __init__(self, author, title, description,author_id,_id=None):
        self.author=author
        self.author_id=author_id
        self.title=title
        self.description=description
        self._id=uuid.uuid4().hex if _id is None else _id

    def new_post(self,title,content,date):
        if date=="":
            date=datetime.datetime.utcnow()
        else:
            datetime.datetime.strptime(date,"%d%m%Y")
        post=Post(blog_id=self._id,
                  title=title,
                  content=content,
                  author=self.author,
                  created_date=date)
        # strptime is string parse time of a date to a format %x = 2 digits for the thing
        post.save_to_mongo()

    def get_posts(self):
        return Post.from_blog(self._id)

    def save_to_mongo(self):
        Database.insert(collection='blogs',data=self.json())

    def json(self):
        return {
            'author':self.author,
            'author_id':self.author_id,
            'title':self.title,
            'description':self.description,
            '_id':self._id
        }

    @classmethod
    def from_mongo(cls,id):
        blog_data=Database.find_one(collection="blogs", query={'_id':id})
        return cls(**blog_data)
        """
                    author=blog_data['author'],
                    title=blog_data['title'],
                    description=blog_data['description'],
                    _id=blog_data['_id']
        """

    @classmethod
    def find_by_author_id(cls, author_id):
        blogs=Database.find(collection="blogs",
                                query={'author_id':author_id})
        return [cls(**blog) for blog in blogs]