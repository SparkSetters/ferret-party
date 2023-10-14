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
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from typing import List

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
llm = OpenAI(openai_api_key=OPENAI_API_KEY)

prompt = PromptTemplate(
    input_variables=["industry1", "industry2", "topic", "exclusion1", "exclusion2", "date_start", "date_end"],
    template=("List 5 emerging or smaller-scale {industry1} or {industry2}-focused {topic} projects between {date_start} and {date_end} that have formed tangible partnerships with traditional Web2 companies. "
              "Exclude major brands or projects like {exclusion1} or {exclusion2}. "
              "For each example, provide: "
              "- The {topic} project name and its financial metrics (e.g., recent funding, valuation, revenue). "
              "- The Web2 partner and a brief description of the partnership. "
              "- The outcome or benefits of the partnership for both parties. "
              "- Duration of the partnership. "
              "- Feedback or reviews from users or customers. "
              "- Any challenges faced and how they were addressed. "
              "- The unique selling proposition (USP) of the partnership. "
              "- A link or reference to the source of the information.")
)

chain = LLMChain(llm=llm, prompt=prompt)

class TestResponse(BaseModel):
    message: str

allowedOrigins = [
    "http://127.0.0.1/:*",
    "http://127.0.0.1:3000",
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

class LLMResponse(BaseModel):
    results: List[str]

class LLMController(Controller):
    @get(path="/llm_results", status_code=HTTP_200_OK)
    async def get_llm_results(self) -> LLMResponse:
        response = chain.run({
            'topic': "NFT", 
            'industry1': "Web3", 
            'industry2': "NFT", 
            'exclusion1': "OpenSea", 
            'exclusion2': "CryptoPunks", 
            'date_start': "January 2023", 
            'date_end': "December 2023"
        })
        return LLMResponse(results=response)


if __name__ == "__main__":
    app = Litestar(route_handlers=[LLMController],
                   cors_config=cors_config
                   )
    response = chain.run({
        'topic': "NFT", 
        'industry1': "Web3", 
        'industry2': "NFT", 
        'exclusion1': "OpenSea", 
        'exclusion2': "CryptoPunks", 
        'date_start': "January 2023", 
        'date_end': "December 2023"
    })
    print(response)