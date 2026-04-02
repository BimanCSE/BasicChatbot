import json
import streamlit as st


class DisplayResultStreamlit:
    def __init__(self, graph, usecase, user_message):
        self.graph = graph
        self.usecase = usecase
        self.user_message = user_message

    def display_result(self):
        """
        Display the result of the graph
        """
        if self.usecase == "Basic Chatbot":
            for event in self.graph.stream({"messages": ("user", self.user_message)}):
                for value in event.values():
                    with st.chat_message("user"):
                        st.write(self.user_message)
                    with st.chat_message("assistant"):
                        st.write(value["messages"].content)
