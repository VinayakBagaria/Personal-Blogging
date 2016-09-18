import pymongo


class Database(object):
    URI="mongodb://127.0.0.1:27017"
    DATABASE=None

    # never show this method to any instance of the database class
    @staticmethod
    def initalise():
        # Since URI is static, defined inside the class but not a method
        client=pymongo.MongoClient(Database.URI);
        Database.DATABASE=client['tutorial']

    @staticmethod
    def insert(collection,data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

