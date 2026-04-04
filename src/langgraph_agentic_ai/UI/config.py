from dotenv import load_dotenv
import os

load_dotenv("/Users/biman_giri/Documents/OfficeWork/BasicChatbot/.env")


class ConfigClass:
    llm_api_key = os.getenv("OPENAI_API_TOKEN")
    lln_api_base_url = os.getenv("OPENAI_API_BASE")
    langsmith_traching = os.getenv("LANGSMITH_TRACING")
    langsmith_api_key = os.getenv("LANGSMITH_API_KEY")
    langsmith_project = os.getenv("LANGSMITH_PROJECT")
    langsmith_endpoint = os.getenv("LANGSMITH_ENDPOINT")

    llm_model_name = ["gpt-4o", "gpt-4o-mini"]
    use_case_option = ["Basic Chatbot", "Chatbot with tool"]
    page_title = "Langgraph : Build stateful agentic ai system"
    llm_option = ["Openai"]
