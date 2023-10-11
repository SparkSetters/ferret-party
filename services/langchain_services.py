from langchain.llms import OpenAI
from langchain.agents import AgentType
from langchain.agents import load_tools
from langchain.agents import initialize_agent
# from tools.google_tool import tools as bstool
from langchain.agents import Tool
from langchain.utilities import GoogleSearchAPIWrapper

# from ..tools.google_tool import tools


def searchQuery():
    llm = OpenAI(model="text-davinci-003", temperature=0)
    search = GoogleSearchAPIWrapper()

    tools = Tool(
        name="Google Search",
        description="Search Google for recent results.",
        func=search.run,
    )

    llm = OpenAI(model="text-davinci-003", temperature=0)
    search = GoogleSearchAPIWrapper()

    agent = initialize_agent([tools],
                             llm,
                             agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
                             verbose=True,
                             max_iterations=6)

    response = agent(
        "DOES COUNTY OF san bernardino ALLOW COMMERCIAL USAGE OF GIS DATA")
    print(response['output'])
