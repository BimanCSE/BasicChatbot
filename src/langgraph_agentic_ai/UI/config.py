from dotenv import load_dotenv
from enum import Enum
import os

load_dotenv("/Users/biman_giri/Documents/OfficeWork/BasicChatbot/.env")


class UsecaseEnum(Enum):
    BASIC_CHATBOT = "Basic Chatbot"
    CHATBOT_WITH_CALCULATOR_TOOL = "Chatbot with calculator tool"
    CHATBOT_WITH_WEB_SEARCH_TOOL = "Chatbot with web search tool"


class ConfigClass:
    llm_api_key = os.getenv("OPENAI_API_TOKEN")
    lln_api_base_url = os.getenv("OPENAI_API_BASE")
    langsmith_traching = os.getenv("LANGSMITH_TRACING")
    langsmith_api_key = os.getenv("LANGSMITH_API_KEY")
    langsmith_project = os.getenv("LANGSMITH_PROJECT")
    langsmith_endpoint = os.getenv("LANGSMITH_ENDPOINT")

    llm_model_name = ["gpt-4o", "gpt-4o-mini"]
    use_case_option = [
        UsecaseEnum.BASIC_CHATBOT,
        UsecaseEnum.CHATBOT_WITH_CALCULATOR_TOOL,
        UsecaseEnum.CHATBOT_WITH_WEB_SEARCH_TOOL,
    ]
    page_title = "Langgraph : Build stateful agentic ai system"
    llm_option = ["Openai"]
    tavily_api_key = os.getenv("TAVILY_API_KEY")
