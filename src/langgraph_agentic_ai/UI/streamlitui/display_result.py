import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.messages import ToolMessage


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
        if self.usecase in ("Basic Chatbot", "Chatbot with tool"):
            self._display_chat_history()

            with st.chat_message("user"):
                st.write(self.user_message)

            response = self.graph.invoke(
                {"messages": [HumanMessage(content=self.user_message)]},
                config=self.config,
            )

            with st.chat_message("assistant"):
                st.write(response["messages"][-1].content)

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
