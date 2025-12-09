from mcp.server.fastmcp import FastMCP

mcp = FastMCP("math-calculator")

@mcp.tool()
def add(x, y):
    """Adds two numbers."""
    return x + y

@mcp.tool()
def subtract(x, y):
    """Subtracts the second number from the first."""
    return x - y

@mcp.tool()
def multiply(x, y):
    """Multiplies two numbers."""
    return x * y

@mcp.tool()
def divide(x, y):
    """Divides the first number by the second."""

    if y == 0:
        return "Error: Cannot divide by zero!"
    return x / y

@mcp.tool()
def power(x, y):
    """Raises the first number to the power of the second."""

    return pow(x, y)


if __name__ == "__main__":
    mcp.run(transport="stdio")