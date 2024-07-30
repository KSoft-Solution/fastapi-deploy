from pymongo import MongoClient

from app.core.basic_config import MONGO_DATABASE

class PyMongoBaseRepo:
    def __init__(self, mongo: MongoClient):
        self._mongo = mongo
        self.database = self._mongo[MONGO_DATABASE]

    @property
    def mongo_client(self) -> MongoClient:
        return self._mongo
