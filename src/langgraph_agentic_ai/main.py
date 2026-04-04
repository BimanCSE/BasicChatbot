import streamlit as st
from src.langgraph_agentic_ai.UI.streamlitui.load_ui import LoadStreamlitUI
from src.langgraph_agentic_ai.LLMs.opeinai_llm_connect import OpenAILLMModel
from src.langgraph_agentic_ai.graph.graph_builder import GraphBuilder
from src.langgraph_agentic_ai.UI.streamlitui.display_result import (
    DisplayResultStreamlit,
)
from langgraph.checkpoint.memory import InMemorySaver

checkpointer_memory = InMemorySaver()


def load_langgraph_agentic_ai_app():
    """
    Loads and runs the streamlit Agentic AI application with Streamlit ui
    This function initialize the UI , handles user input , configure the LLM Model,
    set up the graph based on the selected use case , and display the output while implementing
    exception handling for robustness
    """

    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()
    if not user_input:
        st.error("Error : Failed to userinput from the ui ")
        return
    user_message = st.chat_input("Enter your message")
    if user_message:
        try:
            ### cofigure the llm model

            obj_llm_config = OpenAILLMModel(user_control_input=user_input)
            model = obj_llm_config.load_llm_model()
            if not model:
                st.error("Error : failed to load the model")
                return

            ### initialize the graph based on the selected use case

            usecase = user_input["selected_usecase"]
            if not usecase:
                st.error("Error : Failed to select the use case")
                return
            graph_builder = GraphBuilder(
                model=model, checkpointer_memory=checkpointer_memory
            )
            try:
                graph = graph_builder.setup_graph(usecase=usecase)
                display_result = DisplayResultStreamlit(
                    graph=graph,
                    usecase=usecase,
                    user_message=user_message,
                    checkpointer_memory=checkpointer_memory,
                )
                display_result.display_result()
            except Exception as e:
                st.error(f"Error : graph set up failed - {e}")
                return

        except Exception as e:
            st.error(f"Error : {e}")
            return
