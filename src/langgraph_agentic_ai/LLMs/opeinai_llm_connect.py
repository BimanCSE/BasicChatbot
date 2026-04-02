import os
import streamlit as st
from langchain_openai import ChatOpenAI


class OpenAILLMModel:
    def __init__(self, user_control_input):
        self.user_control_input = user_control_input

    def load_llm_model(self):
        try:
            api_key = self.user_control_input["api_key"]
            base_url = self.user_control_input["api_base_url"]
            model_name = self.user_control_input["selected_llm_model"]
            if api_key == "" or base_url == "" or model_name == "":
                st.error(
                    "please check if you enter the api key , base url or llm model correctly or not"
                )

            llm_model = ChatOpenAI(
                api_key=api_key, base_url=base_url, model=model_name, temperature=0.0
            )
            return llm_model
        except Exception as e:
            raise Exception("Error in LLM model loading", e)
