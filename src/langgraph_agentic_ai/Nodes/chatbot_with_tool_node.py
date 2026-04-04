from src.langgraph_agentic_ai.State.state import State
from src.langgraph_agentic_ai.tools.calculator_tool import (
    addition_tool,
    subtraction_tool,
    multiplication_tool,
    division_tool,
)


class ChatbotWithToolNode:
    """
    Chatbot with tool logic implementation
    """

    def __init__(self, model, tools):
        self.llm_model = model.bind_tools(tools)

    def process(self, state: State):
        """
        Process the input state and generates a chatbot response with tool integration.
        """
        response = self.llm_model.invoke(state["messages"])
        return {"messages": [response]}
