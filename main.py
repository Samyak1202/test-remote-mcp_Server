# from fastmcp import FastMCP
# import math

# # Create MCP server
# mcp = FastMCP("AsyncCalculatorServer")


# # ✅ Helper for type validation
# def validate_number(value, name="value"):
#     if not isinstance(value, (int, float)):
#         raise TypeError(f"{name} must be int or float")
#     return float(value)


# # ➕ Addition
# @mcp.tool()
# async def add(a, b):
#     """Add two numbers"""
#     a = validate_number(a, "a")
#     b = validate_number(b, "b")
#     return a + b


# # ➖ Subtraction
# @mcp.tool()
# async def subtract(a, b):
#     """Subtract two numbers"""
#     a = validate_number(a, "a")
#     b = validate_number(b, "b")
#     return a - b


# # ✖️ Multiplication
# @mcp.tool()
# async def multiply(a, b):
#     """Multiply two numbers"""
#     a = validate_number(a, "a")
#     b = validate_number(b, "b")
#     return a * b


# # ➗ Division
# @mcp.tool()
# async def divide(a, b):
#     """Divide two numbers"""
#     a = validate_number(a, "a")
#     b = validate_number(b, "b")

#     if b == 0:
#         raise ValueError("Division by zero is not allowed")

#     return a / b


# # 🔢 Power
# @mcp.tool()
# async def power(base, exponent):
#     """Raise base to the power of exponent"""
#     base = validate_number(base, "base")
#     exponent = validate_number(exponent, "exponent")
#     return base ** exponent


# # √ Square Root
# @mcp.tool()
# async def sqrt(x):
#     """Calculate square root"""
#     x = validate_number(x, "x")

#     if x < 0:
#         raise ValueError("Cannot take sqrt of negative number")

#     return math.sqrt(x)


# # 🎯 Async main function
# def main():
#     print("🚀 Starting Async FastMCP Calculator Server...")
#     mcp.run()


# # ✅ NO asyncio.run()
# if __name__ == "__main__":
#     main()

from fastmcp import FastMCP
import random
import json

mcp = FastMCP("Simple Calculator server")
@mcp.tool()
def add(a:int, b:int)->int:
    """Add two number together.
    Args:
    a:first_number
    b: second_number
    Returns:
    The sum of a and b
    """
    return a+b

@mcp.tool()
def random_number(min_val:int = 1, max_val:int = 100)->int:
    """Generate a random number within a range.
    Args:
    min_val: minimum value by default is 1
    max_val: maximum value by default is 100
    
    Returns:
    A random integer between min_val and max_val"""
    return random.randint(min_val, max_val)

@mcp.resource("info://server")
def server_info()->str:
    """Get information about this server."""
    info = {
        "name":"simple Calculator server",
        "version":"1.0.0",
        "description":"A basic MCP server with math tools",
        "tools":["add", "random_number"],
        "author":"Your name"
    }
    return json.dumps(info, indent=2)

if __name__ == "__main__":
    mcp.run(transport = "http", host = "0.0.0.0", port = 8000)