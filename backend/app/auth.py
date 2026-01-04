from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import jwt

from .settings import settings

bearer = HTTPBearer()

def get_current_user_id(creds: HTTPAuthorizationCredentials = Depends(bearer)) -> int:
    token = creds.credentials
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=["HS256"])
        user_id = payload.get("sub") or payload.get("user_id")
        if not user_id:
            raise ValueError("Missing user identifier")
        return int(user_id)
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
