import streamlit as st
import os
from src.langgraph_agentic_ai.UI.config import ConfigClass
from src.langgraph_agentic_ai.UI.config import UsecaseEnum


class LoadStreamlitUI:

    def __init__(self):
        self.config = ConfigClass()
        self.user_control = {}

    def load_streamlit_ui(self):
        st.set_page_config(page_title=self.config.page_title, layout="wide")
        st.header(" " + self.config.page_title)
        st.session_state.timeframe = None
        st.session_state.IsFetchButtonClicked = False
        with st.sidebar:
            ### get options from config
            llm_options = self.config.llm_option
            use_case_option = self.config.use_case_option
            ### LLM selection
            self.user_control["selected_llm"] = st.selectbox("Select LLM", llm_options)
            if self.user_control["selected_llm"] == "Openai":
                model_options = self.config.llm_model_name
                self.user_control["selected_llm_model"] = st.selectbox(
                    "Select Model", model_options
                )
                self.user_control["api_base_url"] = st.text_input(
                    value=self.config.lln_api_base_url, type="default", label="base_url"
                )
                self.user_control["api_key"] = st.text_input(
                    value=self.config.llm_api_key, type="password", label="api_key"
                )

            self.user_control["selected_usecase"] = st.selectbox(
                "Select Usecases", use_case_option
            )
            if (
                self.user_control["selected_usecase"]
                == UsecaseEnum.CHATBOT_WITH_WEB_SEARCH_TOOL
                or self.user_control["selected_usecase"]
                == UsecaseEnum.CHATBOT_WITH_AI_NEWS_SUMMARIZER_TOOL
            ):
                self.user_control["tavily_api_key"] = st.text_input(
                    value=self.config.tavily_api_key,
                    type="password",
                    label="tavily_api_key",
                )
                os.environ["TAVILY_API_KEY"] = self.user_control["tavily_api_key"]
            if (
                self.user_control["selected_usecase"]
                == UsecaseEnum.CHATBOT_WITH_AI_NEWS_SUMMARIZER_TOOL
            ):
                st.subheader("News Timeline Options")
                time_frame = st.selectbox(
                    "Select News Timeline", ["Daily", "Weekly", "Monthly"]
                )
                if st.button("Fetch News", use_container_width=True):
                    st.session_state.IsFetchButtonClicked = True
                    st.session_state.time_frame = time_frame
        return self.user_control
