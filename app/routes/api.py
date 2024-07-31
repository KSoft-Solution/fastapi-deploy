from fastapi import APIRouter, Request

from app.routes.user import user_router

router = APIRouter()

router.include_router(user_router, tags=["USER"], prefix="/v1/user")

@router.get(
    "/",
    name="root"
)
def hello_world(request: Request):
    return {"message": "Hello World", "root_path": request.scope.get("root_path")}