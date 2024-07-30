import datetime
from typing import Any,Optional
from datetime import datetime
from pydantic import EmailStr,BaseModel

class CreateUserRequest(BaseModel):
    email: EmailStr
    password: Optional[str]
    username: str

class CreateUserResponse(BaseModel):    
    created: datetime 
    modified: datetime 
    username: str 
    email: EmailStr
    hashed_password: Any 
    email_validated: bool
    is_active: bool
    is_superuser: bool 
    refresh_tokens: list
