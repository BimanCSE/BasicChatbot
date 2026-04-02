from pydantic import BaseModel
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages
from typing import Annotated, List


class State(TypedDict):
    """
    Represent the structure of the state used in the graph
    """

    messages: Annotated[list, add_messages]
