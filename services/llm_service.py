from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os

def run_llm_chain():
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    llm = OpenAI(openai_api_key=OPENAI_API_KEY)
    prompt = PromptTemplate(
        input_variables=["industry1", "industry2", "topic", "exclusion1", "exclusion2", "date_start", "date_end"],
        template=("List 1 emerging or smaller-scale {industry1} or {industry2}-focused {topic} projects between {date_start} and {date_end} that have formed tangible partnerships with traditional Web2 companies."
                "Exclude major brands or projects like {exclusion1} or {exclusion2}. "
                #   "For each example, provide: "
                #   "- The {topic} project name and its financial metrics (e.g., recent funding, valuation, revenue). "
                #   "- The Web2 partner and a brief description of the partnership. "
                #   "- The outcome or benefits of the partnership for both parties. "
                #   "- Duration of the partnership. "
                #   "- Feedback or reviews from users or customers. "
                #   "- Any challenges faced and how they were addressed. "
                #   "- The unique selling proposition (USP) of the partnership. "
                #   "- A link or reference to the source of the information."
        ))

    chain = LLMChain(llm=llm, prompt=prompt)

    response = chain.run({
        'topic': "NFT", 
        'industry1': "Web3", 
        'industry2': "NFT", 
        'exclusion1': "OpenSea", 
        'exclusion2': "CryptoPunks", 
        'date_start': "January 2023", 
        'date_end': "December 2023"
    })
    return response


