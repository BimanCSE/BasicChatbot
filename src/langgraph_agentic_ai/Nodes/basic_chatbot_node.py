from src.langgraph_agentic_ai.State.state import State


class BasicChatbotNode:
    """
    Basic chatbot logic implementation
    """

    def __init__(self, model):
        self.llm_model = model

    def process(self, state: State):
        """
        Process the input state and generates a chatbot response
        """
        response = self.llm_model.invoke(state["messages"])
        return {"messages": [response]}
