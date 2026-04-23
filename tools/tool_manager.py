from langchain_core.tools import tool
import ast
import math

@tool
def calculate(expression: str) -> str:
    """Evaluate a math expression safely."""
    try:
        node = ast.parse(expression, mode='eval')
        # Whitelist allowed functions
        allowed_functions = {
            'sqrt': math.sqrt,
            'pow': math.pow,
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'exp': math.exp,
            'log': math.log,
            'log10': math.log10
        }

        # Create a safe namespace
        safe_namespace = {
            '__builtins__': {'abs': abs, 'float': float, 'int': int},
            **allowed_functions
        }

        code = compile(node, '<string>', 'eval')
        result = eval(code, safe_namespace)
        return str(result)
    except Exception as e:
        return f"Error: {e}"

def get_tools():
    return [calculate]