# app/core/security.py

from fastapi import Depends, HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from app.core.config import settings
from typing import Optional
from pydantic import BaseModel
import requests

security = HTTPBearer()

class TokenData(BaseModel):
    user_id: Optional[str] = None

def verify_token(token: str) -> TokenData:
    try:
        payload = jwt.decode(token, settings.SUPABASE_JWT_SECRET, algorithms=[settings.SUPABASE_JWT_ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Token is invalid")
        return TokenData(user_id=user_id)
    except JWTError:
        raise HTTPException(status_code=401, detail="Token is invalid")

def get_current_user(credentials: HTTPAuthorizationCredentials = Security(security)) -> TokenData:
    return verify_token(credentials.credentials)