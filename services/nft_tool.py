from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os


class NFTTool:
    def __init__(self, api_key=None):
        self.api_key = api_key if api_key else os.getenv("OPENAI_API_KEY")
        self.llm = OpenAI(openai_api_key=self.api_key)

    def set_prompt_template(self, input_variables, template):
        self.prompt = PromptTemplate(input_variables=input_variables, template=template)

    def set_chain(self):
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)

    def run(
        self, topic, industry1, industry2, exclusion1, exclusion2, date_start, date_end
    ):
        self.set_prompt_template(
            input_variables=[
                "industry1",
                "industry2",
                "topic",
                "exclusion1",
                "exclusion2",
                "date_start",
                "date_end",
            ],
            template=(
                "List 1 emerging or smaller-scale {industry1} or {industry2}-focused {topic} projects between {date_start} and {date_end} that have formed tangible partnerships with traditional Web2 companies."
                "Exclude major brands or projects like {exclusion1} or {exclusion2}."
            ),
        )
        self.set_chain()

        response = self.chain.run(
            {
                "topic": topic,
                "industry1": industry1,
                "industry2": industry2,
                "exclusion1": exclusion1,
                "exclusion2": exclusion2,
                "date_start": date_start,
                "date_end": date_end,
            }
        )

        return response


if __name__ == "__main__":
    nft_tool = NFTTool()
    response = nft_tool.run(
        topic="NFT",
        industry1="Web3",
        industry2="NFT",
        exclusion1="OpenSea",
        exclusion2="CryptoPunks",
        date_start="January 2023",
        date_end="December 2023",
    )
    print("Response:", response)
