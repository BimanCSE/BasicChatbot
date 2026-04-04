from langchain_tavily import TavilySearch
from src.langgraph_agentic_ai.State.state import State
from langgraph.prebuilt import ToolNode


def tavily_web_search_tool():
    """
    Creates a tavily web search tool that uses the tavily web search tool.
    """
    tavily_search = TavilySearch(max_results=5)
    return tavily_search


def create_tavily_web_search_node():
    """
    Creates a tavily web search node that uses the tavily web search tool.
    """
    tavily_web_search_node = ToolNode(tools=[tavily_web_search_tool()])
    return tavily_web_search_node
