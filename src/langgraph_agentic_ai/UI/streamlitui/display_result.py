import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.messages import ToolMessage
from src.langgraph_agentic_ai.UI.config import UsecaseEnum
from pprint import pprint


class DisplayResultStreamlit:
    def __init__(self, graph, usecase, user_message, checkpointer_memory):
        self.graph = graph
        self.usecase = usecase
        self.user_message = user_message
        self.checkpointer_memory = checkpointer_memory
        self.config = {"configurable": {"thread_id": "1"}}

    def display_result(self):
        """
        Display the result of the graph
        """
        if self.usecase in (
            UsecaseEnum.BASIC_CHATBOT,
            UsecaseEnum.CHATBOT_WITH_CALCULATOR_TOOL,
            UsecaseEnum.CHATBOT_WITH_WEB_SEARCH_TOOL,
        ):
            self._display_chat_history()

            with st.chat_message("user"):
                st.write(self.user_message)

            response = self.graph.invoke(
                {"messages": [HumanMessage(content=self.user_message)]},
                config=self.config,
            )
            for msg in response["messages"]:
                msg.pretty_print()
            with st.chat_message("assistant"):
                st.write(response["messages"][-1].content)
        elif self.usecase == UsecaseEnum.CHATBOT_WITH_AI_NEWS_SUMMARIZER_TOOL:
            print(self.user_message)
            frequency = self.user_message
            with st.spinner("Fetching and summarizing news .... "):
                result = self.graph.invoke(
                    {"frequency": frequency},
                    config=self.config,
                )
            st.markdown(result["summary"], unsafe_allow_html=True)
            st.download_button(
                label="Download News Summary",
                data=result["saved_file_name"],
                file_name=result["saved_file_name"],
            )

    def _display_chat_history(self):
        """
        Retrieve and display previous messages from checkpointer memory.
        """
        state = self.graph.get_state(self.config)
        if state.values and "messages" in state.values:
            for msg in state.values["messages"]:
                if isinstance(msg, AIMessage):
                    with st.chat_message("assistant"):
                        st.write(msg.content)
                elif isinstance(msg, HumanMessage):
                    with st.chat_message("user"):
                        st.write(msg.content)
                elif isinstance(msg, ToolMessage):
                    st.write(msg.content)
