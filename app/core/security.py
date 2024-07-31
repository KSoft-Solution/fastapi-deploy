from datetime import datetime, timedelta
from jose import jwt 
from passlib.context import CryptContext
from typing import Union, Any

from app.core.basic_config import ACCESS_TOKEN_EXPIRE_MINUTES,ALGORITHM,JWT_SECRET_KEY,REFRESH_TOKEN_EXPIRE_MINUTES,JWT_REFRESH_SECRET_KEY

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Create Access Token
def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
        print(f"expire: {expire}")
    else:
        expire = datetime.utcnow() + timedelta(ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=ALGORITHM)
    print(f"encoded_jwt: {encoded_jwt}")
    return encoded_jwt


#  Create Refresh Token
def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
        print(f"expire: {expire}")
    else:
        expire = datetime.utcnow() + timedelta(REFRESH_TOKEN_EXPIRE_MINUTES)
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, algorithm=ALGORITHM)
    print(f"encoded_jwt: {encoded_jwt}")
    return encoded_jwt


# Verify Password
def verify_password(password: str, hashed: str) -> bool:
    return password_context.verify(password, hashed)


# Get Password Hash
def get_password_hash(password: str) -> str:
    print(f"getPasswordHash: {password}")
    return password_context.hash(password)
