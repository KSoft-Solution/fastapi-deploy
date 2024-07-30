from fastapi import APIRouter, Depends
from starlette.status import HTTP_200_OK

router = APIRouter()

@router.get(
    '/',
    status_code=HTTP_200_OK,
    response_description="create user",
    name="user:create",
    response_model_exclude_none=True,
    # response_model=CreateUserResponse,
)
def create_user_api():
    return {"hello":"world"}
