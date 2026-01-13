from flask import g, request
from functools import wraps
import jwt
import os

def auth_middleware(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # TODO: Implement authentication middleware
        # use request.headers
        # Exceptions thrown by jwt decode: jwt.ExpiredSignatureError, jwt.InvalidTokenError:
        # pass things in using g.username
        key = request.headers.get("Authorization")
        JWTtemp = key.substring[7:]
        try {
            g.username = jwt.decode(JWTtemp, "loggedIn", algorithm="HS256")["username"]
        }
        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError) {
            return "Expired or Invalid Token", 401
        }
        
        return f(*args, **kwargs)
    
    return decorated_function
