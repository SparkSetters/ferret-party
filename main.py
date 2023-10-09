import os
from litestar import Controller, get, Litestar, Request
from pydantic import BaseModel
from litestar.config.cors import CORSConfig
from litestar.types import ASGIApp, Scope, Receive, Send
from litestar.exceptions import NotAuthorizedException
from jose import jwt, JWTError
from typing import Callable
from litestar.config.allowed_hosts import AllowedHostsConfig
from litestar.status_codes import HTTP_200_OK


class TestResponse(BaseModel):
    message: str


allowedOrigins = [
    "http://127.0.0.1/:*",
    "http://127.0.0.1:8100",
    'capacitor://localhost',
    'ionic://localhost',
    'http://localhost',
    'http://localhost:8080',
    'http://localhost:8100',
]

cors_config = CORSConfig(allow_origins=allowedOrigins,
                         allow_methods=["*"],
                         allow_headers=["Authorization", "Content-Type"],
                         allow_credentials=True,
                         expose_headers=[],
                         max_age=600)


# def validate_jwt(request: Request) -> bool:
#     token = request.headers.get("Authorization", "")
#     # print("token here" + request.headers)
#     if not token:
#         raise NotAuthorizedException("JWT not found in headers.")

#     token = token.replace("Bearer ", "")
#     JWT_SECRET = os.environ.get("SUPABASE_JWT_SECRET")
#     JWT_ALGORITHM = os.environ.get("SUPABASE_JWT_ALGORITHM")

#     if not JWT_SECRET or not JWT_ALGORITHM:
#         raise NotAuthorizedException("Invalid JWT configuration.")

#     try:
#         decoded = jwt.decode(token, JWT_SECRET, algorithms=JWT_ALGORITHM)
#         return True
#     except JWTError:
#         raise NotAuthorizedException("Invalid JWT token.")


# def jwt_authentication_middleware_factory(app: ASGIApp) -> ASGIApp:
#     async def jwt_authentication_middleware(scope: Scope, receive: Receive, send: Send) -> None:
#         request = Request(scope, receive=receive)
#         try:
#             print(await scope)
#             validate_jwt(request)
#             await app(scope, receive, send)
#         except NotAuthorizedException as e:
#             raise e

#     return jwt_authentication_middleware


class MyTest(Controller):
    @get(path="/", status_code=HTTP_200_OK)
    def validate_route_handler(self) -> TestResponse:
        return TestResponse(message="Response from Litestar")


app = Litestar(route_handlers=[MyTest],
               cors_config=cors_config
               )
