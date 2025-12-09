# Math Calculator MCP Server

An MCP (Model Context Protocol) server that provides math calculation tools to Claude.

## Tools Available

- `add`: Adds two numbers
- `subtract`: Subtracts the second number from the first
- `multiply`: Multiplies two numbers
- `divide`: Divides the first number by the second (with zero-division protection)
- `power`: Raises the first number to the power of the second

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   # or
   uv sync
   ```

2. Test the server locally:
   ```bash
   python math.py
   ```

## Connecting to Claude Desktop

To use this MCP server with Claude Desktop, you need to add it to your Claude Desktop configuration.

### Step 1: Locate Claude Desktop Config File

On Windows, the config file is located at:
```
%APPDATA%\Claude\claude_desktop_config.json
```

Full path is typically:
```
C:\Users\<YourUsername>\AppData\Roaming\Claude\claude_desktop_config.json
```

### Step 2: Edit the Config File

Open `claude_desktop_config.json` in a text editor. If it doesn't exist, create it.

### Step 3: Add Your MCP Server Configuration

Add the following configuration to the `mcpServers` object:

```json
{
  "mcpServers": {
    "math-calculator": {
      "command": "python",
      "args": [
        "D:\\BAVE AI\\MCP-Practice\\math.py"
      ],
      "env": {}
    }
  }
}
```

**Important Notes:**

1. **Using Virtual Environment**: If you're using a virtual environment (recommended), update the path to use the Python interpreter from your venv:

   ```json
   {
     "mcpServers": {
       "math-calculator": {
         "command": "D:\\BAVE AI\\MCP-Practice\\.venv\\Scripts\\python.exe",
         "args": [
           "D:\\BAVE AI\\MCP-Practice\\math.py"
         ],
         "env": {}
       }
     }
   }
   ```

2. **Path Format**: On Windows, use forward slashes `/` or escaped backslashes `\\` in JSON paths.

3. **Example Full Config**: Here's what a complete config file might look like:

   ```json
   {
     "mcpServers": {
       "math-calculator": {
         "command": "D:\\BAVE AI\\MCP-Practice\\.venv\\Scripts\\python.exe",
         "args": [
           "D:\\BAVE AI\\MCP-Practice\\math.py"
         ],
         "env": {}
       }
     }
   }
   ```

### Step 4: Restart Claude Desktop

After saving the configuration file:
1. Close Claude Desktop completely
2. Reopen Claude Desktop
3. The MCP server should automatically connect

### Step 5: Verify Connection

Once connected, you should see the math calculator tools available in Claude. You can test it by asking Claude to perform calculations:

- "Add 5 and 3"
- "Multiply 7 by 8"
- "What's 10 to the power of 3?"

## Troubleshooting

- **Server not connecting**: Check that the Python path and script path are correct in the config
- **Import errors**: Make sure all dependencies are installed in your virtual environment
- **Permission errors**: Ensure the paths in the config file are accessible
