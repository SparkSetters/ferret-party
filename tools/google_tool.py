from langchain.agents import Tool
from langchain.utilities import GoogleSearchAPIWrapper


search = GoogleSearchAPIWrapper()

tools = Tool(
    name="Google Search",
    description="Search Google for recent results.",
    func=search.run,
)

# print(tools.run(
#     "County of Los Angeles' eGIS data commercial terms of use and return the url"))
