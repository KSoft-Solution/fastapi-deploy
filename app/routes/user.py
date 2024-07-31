import pymongo
from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from app.helper.auth import get_current_user
from app.models.user import UserModel
from app.schemas.user import UserOut,UserAuth,UserUpdate
from app.services.user import UserService

user_router = APIRouter()

# @user_router.get(
#     '/list.todos',
#     status_code=HTTP_200_OK,
#     name="todo:list",
#     response_description="list todos",
#     response_model=ListToDoResponse,
#     response_model_exclude_none=True
# )
# def get_todo_list_api(
#     todos: ListToDoResponse = Depends(get_todo_list)
# ):
#     return todos


# @user_router.post(
#     '/todo.create',
#     status_code=HTTP_200_OK,
#     response_description="list todos",
#     name="todo:create",
#     response_model_exclude_none=True,
#     response_model=CreateToDoResponse,
# )
# def create_todo_api(
#     todo: CreateToDoResponse = Depends(create_todo)
# ):
#     return todo


@user_router.post("/create", summary="Create new user", )
async def create_user(data: UserAuth):
    try:
        print(f"data: {data}")
        user = await UserService.create_user(data)
        return {
            "code": 1,
            "message": "Success",
            "data": user
        }
    except pymongo.errors.DuplicateKeyError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this username or email already exists"
        )


@user_router.get("/get_all_users", summary="Get All Users", )
async def get_all_users():
    return {"get_all_users": "Get all users"}


@user_router.get("/me", summary="Get user by email", response_model=UserOut)
def get_me(user: UserModel = Depends(get_current_user)):
    return user


@user_router.get("/user/id", summary="Get user by id")
async def get_user_by_id(userId: int):
    return {"get_user_by_id": f"get user by {userId}"}


@user_router.patch("/update", summary="Update user by email", response_model=UserOut)
async def update_user(data: UserUpdate, user: UserModel = Depends(get_current_user)):
    try:
        return await UserService.update_user(user.user_id, data)
    except pymongo.errors.OperationFailure:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email does not exist"
        )


@user_router.delete("/delete", summary="Delete User", )
async def delete_user():
    return {"delete_user": "Delete User"}

