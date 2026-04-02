from langgraph.graph import StateGraph, START, END
from src.langgraph_agentic_ai.State.state import State
from src.langgraph_agentic_ai.Nodes.basic_chatbot_node import BasicChatbotNode
import streamlit as st


class GraphBuilder:

    def __init__(self, model):
        self.llm_model = model
        self.graph_builder = StateGraph(State)

    def basic_chatbot(self):
        """
        Builds a basic chatbot using langgraph. This method initiates a chabot using
        the 'BasiChatbotNode' class and integrate with the graph . The chatbot is set to be entry and exit point of the graph.
        """
        self.basic_chatbot = BasicChatbotNode(model=self.llm_model)
        self.graph_builder.add_node("chatbot", self.basic_chatbot.process)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)

    def setup_graph(self, usecase):
        """
        Set up the graph based on the selected use case
        """
        if usecase == "Basic Chatbot":
            self.basic_chatbot()
        else:
            st.error("Error : Failed to select the use case")
            return
        return self.graph_builder.compile()
