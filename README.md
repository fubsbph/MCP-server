# MCP Server

A small MCP (Model Context Protocol) server that exposes YouTube transcript, web-search and read/write to the local files tools.

## 🎥 Demos (3 quick videos)

- MCP Inspector:
  https://github.com/user-attachments/assets/cd503d0b-3b67-4e38-b472-12c1a520a326

- Claude Desktop: 
  https://github.com/user-attachments/assets/0a85b309-fbcf-4ce7-ab5f-9f50a62d7652

- Results (saved file):
  https://github.com/user-attachments/assets/1cb82d4f-8ba7-479a-8e4f-c5471cdf66d5

**Requirements**
- **Python**: 3.12 recommended (works with 3.10+).
- **OS**: WSL (recommended) or Windows — prefer running the server in the same environment where the virtualenv lives.
- **Dependencies**: declared in `pyproject.toml` (install with `pip install -e .`).

**Quick Setup (WSL, recommended)**

1. From the project root:

```bash
# remove existing venv if exist one
rm -rf .venv

# create venv with system or pyenv python3.12
uv venv
source .venv/bin/activate
pip install -U pip
pip install -e .
```

2. Run the server from the venv:

```bash
source .venv/bin/activate
mcp dev server.py
```

**Development notes**
- Use the same Python/uv used to create the venv when starting the server.
- Preferred command to run during development (inside WSL venv):

```bash
source .venv/bin/sctivate
uv run --native-tls mcp dev server.py
```
