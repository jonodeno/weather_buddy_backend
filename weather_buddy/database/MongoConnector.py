import os
from pymongo import MongoClient

default_table = os.getenv('MONGO_DEFAULT_TABLE')

class MongoConnector():
    def __init__(self):
        connection_str = f"mongodb+srv://{os.getenv('MONGO_USERNAME')}"\
            f":{os.getenv('MONGO_PWD')}@weatherbuddy.osvfs.mongodb.net/"\
            f"{default_table}?retryWrites=true&w=majority"
        self._client = MongoClient(connection_str)
    
    def get_wb_table(self):
        """
        Returns the default DB
        """
        return self._client[default_table]
    
    def get_collection(self, name):
        """
        Returns a collection based on the name
        """
        return self.get_wb_table()[name]