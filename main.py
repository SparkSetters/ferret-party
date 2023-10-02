import os
from litestar import Controller, get, Litestar, Request
from litestar.types import ASGIApp, Scope, Receive, Send
from litestar.exceptions import NotAuthorizedException
from jose import jwt, JWTError
from typing import Callable


def validate_jwt(request: Request) -> bool:
    token = request.headers.get("Authorization", "")
    if not token:
        raise NotAuthorizedException("JWT not found in headers.")

    token = token.replace("Bearer ", "")
    JWT_SECRET = os.environ.get("SUPABASE_JWT_SECRET")
    JWT_ALGORITHM = os.environ.get("SUPABASE_JWT_ALGORITHM")

    if not JWT_SECRET or not JWT_ALGORITHM:
        raise NotAuthorizedException("Invalid JWT configuration.")

    try:
        decoded = jwt.decode(token, JWT_SECRET, algorithms=JWT_ALGORITHM)
        return True
    except JWTError:
        raise NotAuthorizedException("Invalid JWT token.")


def jwt_authentication_middleware_factory(app: ASGIApp) -> ASGIApp:
    async def jwt_authentication_middleware(scope: Scope, receive: Receive, send: Send) -> None:
        request = Request(scope, receive=receive)
        try:
            validate_jwt(request)
            await app(scope, receive, send)
        except NotAuthorizedException as e:
            raise e

    return jwt_authentication_middleware


class MyTest(Controller):
    @get(path="/")
    def validate_route_handler(self) -> str:
        return "JWT is valid!"


app = Litestar(route_handlers=[MyTest], middleware=[
               jwt_authentication_middleware_factory])
