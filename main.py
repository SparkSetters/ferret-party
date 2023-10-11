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
from tools import google_tool
from services import langchain_services
# from dotenv import load_dotenv

# load_dotenv()

# print(os.environ['ACTIVELOOP_TOKEN'])

# print(os.environ['GOOGLE_API_KEY'])


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


class MyTest(Controller):
    @get(path="/", status_code=HTTP_200_OK)
    async def validate_route_handler(self) -> TestResponse:
        return TestResponse(message="Response from Litestar")


app = Litestar(route_handlers=[MyTest],
               cors_config=cors_config
               )

# netu example crap


def search_google(query):
    tool = google_tool.get_search_tool()
    result = tool.run(query)
    return result


if __name__ == "__main__":
    # query = "OpenAI GPT-4 capabilities"
    langchain_services.searchQuery()
    # print(response)
