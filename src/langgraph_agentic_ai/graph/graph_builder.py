from langgraph.graph import StateGraph, START, END
from src.langgraph_agentic_ai.State.state import State
from src.langgraph_agentic_ai.Nodes.basic_chatbot_node import BasicChatbotNode
import streamlit as st
from src.langgraph_agentic_ai.Nodes.calculator_tool_node import (
    create_calculator_tool_node,
)
from langgraph.prebuilt import ToolNode, tools_condition
from src.langgraph_agentic_ai.Nodes.chatbot_with_tool_node import ChatbotWithToolNode
from src.langgraph_agentic_ai.UI.config import UsecaseEnum
from src.langgraph_agentic_ai.tools.calculator_tool import (
    addition_tool,
    subtraction_tool,
    multiplication_tool,
    division_tool,
)
from src.langgraph_agentic_ai.Nodes.trvily_web_search_node import tavily_web_search_tool


class GraphBuilder:

    def __init__(self, model, checkpointer_memory):
        self.llm_model = model
        self.checkpointer_memory = checkpointer_memory
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

    def basic_chatbot_with_tool(self):
        """
        Builds an advanced chatbot graph with tool integration.
        This method creates a chatbot graph that includes both a chatbot node and tool node. it defines tools, initialized the chatbot with tool
        capabilities, and sets up conditional and direct edges between nodes. The chatbot node is set as the entry point.
        """
        # define the tool  and tool node
        calculator_tool_node = create_calculator_tool_node()
        ### define the chat node

        #### add nodes
        self.graph_builder.add_node(
            "chatbot",
            ChatbotWithToolNode(
                model=self.llm_model,
                tools=[
                    addition_tool,
                    subtraction_tool,
                    multiplication_tool,
                    division_tool,
                ],
            ).process,
        )
        self.graph_builder.add_node("tools", calculator_tool_node)

        ### define conditional and direction edges

        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_conditional_edges("chatbot", tools_condition)
        self.graph_builder.add_edge("tools", "chatbot")

    def chatbot_with_web_search_tool(self):
        """
        Builds a chatbot graph with web search tool.
        This method creates a chatbot graph that includes both a chatbot node and web search tool node. it defines tools, initialized the chatbot with tool
        capabilities, and sets up conditional and direct edges between nodes. The chatbot node is set as the entry point.
        """
        search_tool = tavily_web_search_tool()
        chatbot_with_tool_node = ChatbotWithToolNode(
            model=self.llm_model,
            tools=[search_tool],
        ).process
        self.graph_builder.add_node("chatbot", chatbot_with_tool_node)
        self.graph_builder.add_node("tools", ToolNode(tools=[search_tool]))
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_conditional_edges("chatbot", tools_condition)
        self.graph_builder.add_edge("tools", "chatbot")

    def setup_graph(self, usecase):
        """
        Set up the graph based on the selected use case
        """
        if usecase == UsecaseEnum.BASIC_CHATBOT:
            self.basic_chatbot()
        elif usecase == UsecaseEnum.CHATBOT_WITH_CALCULATOR_TOOL:
            self.basic_chatbot_with_tool()
        elif usecase == UsecaseEnum.CHATBOT_WITH_WEB_SEARCH_TOOL:
            self.chatbot_with_web_search_tool()
        else:
            st.error("Error : Failed to select the use case")
            return
        return self.graph_builder.compile(checkpointer=self.checkpointer_memory)
