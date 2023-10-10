from langchain.llms import OpenAI

from langchain.agents import AgentType
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from tools.google_tool import tools
from langchain.agents import Tool
from langchain.utilities import GoogleSearchAPIWrapper
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
    "what is the contact info for the county of san bernardino's office that handles sales of gis data")
print(response['output'])
