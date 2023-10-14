from litestar import Controller, get
from litestar.status_codes import HTTP_200_OK
from models.llm_models import LLMResponse
from services.llm_service import run_llm_chain

class LLMController(Controller):
    @get(path="/llm_results", status_code=HTTP_200_OK)
    async def get_llm_results(self) -> LLMResponse:
        response = run_llm_chain()
        return LLMResponse(results=response)
