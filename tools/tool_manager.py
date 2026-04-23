from langchain_core.tools import tool

@tool
def dummy_tool(input: str) -> str:
    """A placeholder tool.  Always returns a canned response."""
    return "This is a dummy tool. It doesn't do anything useful."

def get_tools():
    return [dummy_tool]