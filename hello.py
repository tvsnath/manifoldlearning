from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool


def add(a,b):
    return a+b

def subtract(a,b):
    return a-b


@tool("add", return_direct=True)
def add_tool(a: int, b: int) -> int:
    """Adds two numbers."""
    return add(a, b)    

@tool("subtract", return_direct=True)
def subtract_tool(a: int, b: int) -> int:
    """Subtracts two numbers."""
    return subtract(a, b)

@tool("get Weather", return_direct=True)
def get_weather(location: str) -> str:
    """Gets the current weather for a given location."""
    # This is a placeholder implementation. In a real application, you would call a weather API.
    return f"The current weather in {location} is sunny with a temperature of 25°C."

print(get_weather.invoke("Fremont"))