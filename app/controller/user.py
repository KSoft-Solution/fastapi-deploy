from datetime import datetime
from fastapi import Depends, Body

from app.db.base import get_mongodb_repo
from app.schemas.user import CreateUserRequest,CreateUserResponse
from app.db.user import UserRepository
from app.models.user import PyObjectId,User

def create_user(
        create_user_req: CreateUserRequest = Body(..., ),
        user_repo: UserRepository = Depends(get_mongodb_repo(UserRepository))
) -> CreateUserResponse:
    user_in_db = User(username=create_user_req.username,
                      password=create_user_req.password,
                      created=datetime.utcnow(),
                    )
    user_created = user_repo.create_user(user_in_db)
    return CreateUserResponse(username=user_created.username)