from crewai.tools import tool 
from tavily import TavilyClient
from dotenv import load_dotenv
import os
load_dotenv()

search_client = TavilyClient(api_key=os.getenv("TVLY_SEARCH_API_KEY"))

@tool
def search_engine_tool(query: str):
    """
    Perform a search for the given query using the configured search client.
    Returns a list of dictionaries, each containing title and url only and score.
    """
    return search_client.search(query=query, max_results=2)  

