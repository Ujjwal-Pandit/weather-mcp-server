# Weather MCP Server - Assignment Project

This project implements MCP (Model Context Protocol) servers for CS 554 Assignment 3.

## Project Structure

- `weather.py` - Weather MCP server (Task 1)
- `calc.py` - Calculator MCP server with SymPy (Task 2)
- `bert_dist.py` - Model distillation implementation (Task 4)

## Setup

### Prerequisites
- Python 3.10 or higher
- `uv` package manager

### Installation on Windows

1. **Install Python 3.10+** (if not already installed):
   - Download from [python.org](https://www.python.org/downloads/) or use the Microsoft Store
   - Make sure to check "Add Python to PATH" during installation

2. **Install `uv` package manager**:
   ```powershell
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```
   **Important**: After installation, restart your terminal/PowerShell for `uv` to be available in PATH.

3. **Install dependencies**:
   ```powershell
   uv sync
   ```

4. **Activate virtual environment** (if needed):
   ```powershell
   # Windows PowerShell
   .venv\Scripts\Activate.ps1
   
   # Windows Command Prompt
   .venv\Scripts\activate.bat
   ```

### Testing with Claude Desktop

For full MCP protocol testing and assignment screenshots, use Claude for Desktop on Windows:

1. **Install Claude for Desktop** from [claude.ai/download](https://claude.ai/download) (if not already installed)

2. **Configure the server** - The configuration has been automatically set up! The config file is at:
   ```
   %AppData%\Claude\claude_desktop_config.json
   ```
   
   Or run the setup script:
   ```powershell
   .\setup_claude_desktop.ps1
   ```

3. **Restart Claude for Desktop** - **IMPORTANT**: Fully quit Claude Desktop (right-click system tray icon → Quit), then restart it. Simply closing the window is not enough.

4. **Test the tools**:
   - Look for the "Search and tools" icon in Claude Desktop
   - Ask Claude: "What are the weather alerts in California?"
   - Or: "What's the weather forecast for New York City?"
   - Take screenshots for your assignment

5. **Verify server is working**:
   ```powershell
   uv run python test_server.py
   ```

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
- For assignment screenshots, test the server using Claude for Desktop and capture the tool calls and results
- All code has been verified to be Windows-compatible (no Linux-specific paths or commands)

## Dependencies

All dependencies are listed in `pyproject.toml`:
- `mcp[cli]` - MCP SDK
- `httpx` - HTTP client for weather API
- `sympy` - Symbolic math for calculator
- `transformers`, `torch`, `datasets` - For model distillation

