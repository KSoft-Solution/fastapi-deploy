from pydantic import ValidationError
from jose import jwt 
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from datetime import datetime

from app.models.user import UserModel
from app.schemas.token import TokenPayload
from app.services.user import UserService
from app.core.basic_config import ALGORITHM, API_V1_STR, JWT_SECRET_KEY

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{API_V1_STR}/auth/login",
    scheme_name="JWT",
)


# Get Current User
async def get_current_user(token: str = Depends(reusable_oauth2)) -> UserModel:
    """
    :param token:
    :return: user
    """
    try:
        payload = jwt.decode(
            token, JWT_SECRET_KEY, algorithms=[ALGORITHM]
        )
        token_data = TokenPayload(**payload)
        if datetime.fromtimestamp(token_data.exp) < datetime.utcnow():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user = await UserService.get_user_by_id(token_data.sub)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find user",
        )
    return user
