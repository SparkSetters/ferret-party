from pydantic import BaseModel
from typing import List

class LLMResponse(BaseModel):
    results: List[str]
