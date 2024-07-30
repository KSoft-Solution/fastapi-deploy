import pymongo
from fastapi.encoders import jsonable_encoder
from pydantic import conint
from pymongo import MongoClient

from app.core.basic_config import MONGO_COLLECTION_USERS
from app.models.base_db import PyMongoBaseRepo
from app.models.user import User

class UserRepository(PyMongoBaseRepo):

    def __int__(self, mongo: MongoClient):
        super().__init__(mongo)

    def list_user(self,
                  sort_field: str = "created_at",
                  sort_order: int = pymongo.DESCENDING,
                  skip: conint(ge=0) = 0,
                  limit: conint(ge=5, multiple_of=5) = 10
                  ):

        todos = self.database[MONGO_COLLECTION_USERS] \
            .find({}) \
            .sort([(sort_field, sort_order)]) \
            .skip(skip).limit(limit)
        total = self.database[MONGO_COLLECTION_USERS].count_documents(filter={})

        return [User(**todo) for todo in todos], total

    def create_user(self, user: User) -> User:
        user_in_db = jsonable_encoder(user)
        new_user = self.database[MONGO_COLLECTION_USERS] \
            .insert_one(document=user_in_db)
        created_user = self.database[MONGO_COLLECTION_USERS].find_one(
            {"_id": new_user.inserted_id}
        )
        return User(**created_user)
