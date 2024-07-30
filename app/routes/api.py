from fastapi import APIRouter, Request

from app.routes import user

router = APIRouter()

router.include_router(user.router, tags=["User"], prefix="/v1/user")

@router.get(
    "/v1/hello",
    name="probe:liveness"
)
def hello_world(request: Request):
    return {"message": "Hello World", "root_path": request.scope.get("root_path")}