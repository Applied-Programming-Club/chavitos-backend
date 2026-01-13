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
        # pass thigns in using g.username

        
        return f(*args, **kwargs)
    
    return decorated_function

def admin_middleware(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # TODO: Implement admin middleware
        
        return f(*args, **kwargs)
    
    return decorated_function
