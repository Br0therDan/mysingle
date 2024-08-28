from fastapi import HTTPException
from jose import JWTError, jwt
from app.core.config import settings

secret = settings.SUPABASE_JWT_SECRET
algorithm = settings.SUPABASE_JWT_ALGORITHM

def verify_token(token: str):
    try:
        payload = jwt.decode(token, secret, algorithms=algorithm)
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token : 토큰검증 실패")