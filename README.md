# Weather MCP Server - Assignment Project

This project implements MCP (Model Context Protocol) servers for CS 554 Assignment 3.

## Project Structure

- `weather.py` - Weather MCP server (Task 1)
- `calc.py` - Calculator MCP server with SymPy (Task 2)
- `bert_dist.py` - Model distillation implementation (Task 4)
- `test_weather_direct.py` - Direct function testing (verifies API connectivity)

## Setup

### Prerequisites
- Python 3.10 or higher
- `uv` package manager

### Installation

```bash
# Install dependencies
uv sync

# Activate virtual environment (if needed)
source .venv/bin/activate
```

## Testing

### Direct Function Testing

Test the weather functions directly to verify API connectivity:

```bash
uv run test_weather_direct.py
```

This directly calls the `get_alerts()` and `get_forecast()` functions and shows their output. Useful for verifying the core functionality works before testing with Claude Desktop.

### Testing with Claude Desktop

For full MCP protocol testing and assignment screenshots, use Claude for Desktop on Windows:

1. Install Claude for Desktop from [claude.ai/download](https://claude.ai/download)
2. Configure the server in `claude_desktop_config.json`:
   ```json
   {
     "mcpServers": {
       "weather": {
         "command": "uv",
         "args": [
           "--directory",
           "C:\\ABSOLUTE\\PATH\\TO\\weather-mcp-server",
           "run",
           "weather.py"
         ]
       }
     }
   }
   ```
3. Restart Claude for Desktop
4. Test the tools and take screenshots for your assignment

## Running the Servers

### Weather Server
```bash
uv run weather.py
```

### Calculator Server
```bash
uv run calc.py
```

## Task Status

- [x] **Task 1**: Weather MCP Server structure created
- [ ] **Task 1**: Testing and screenshots (requires Claude Desktop or alternative)
- [ ] **Task 2**: Complete calculator TODOs
- [ ] **Task 3**: Explore MCP ecosystem (research task)
- [ ] **Task 4**: Complete model distillation TODOs

## Notes

- The weather server is ready to use with Claude for Desktop on Windows
- Use `test_weather_direct.py` to verify API connectivity before testing with Claude Desktop
- For assignment screenshots, test the server using Claude for Desktop and capture the tool calls and results

## Dependencies

All dependencies are listed in `pyproject.toml`:
- `mcp[cli]` - MCP SDK
- `httpx` - HTTP client for weather API
- `sympy` - Symbolic math for calculator
- `transformers`, `torch`, `datasets` - For model distillation

