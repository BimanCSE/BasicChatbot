from src.langgraph_agentic_ai.tools.calculator_tool import (
    addition_tool,
    subtraction_tool,
    multiplication_tool,
    division_tool,
)
from langgraph.prebuilt import ToolNode


def create_calculator_tool_node():
    """
    Creates a calculator tool node that uses the calculator tools.
    """
    calculator_tool_node = ToolNode(
        tools=[addition_tool, subtraction_tool, multiplication_tool, division_tool]
    )
    return calculator_tool_node
