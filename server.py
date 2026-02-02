# /// script for Claude MCP server to connect
# requires-python = ">=3.10"
# dependencies = [
#     "ddgs>=9.10.0",
#     "mcp[cli]>=1.25.0",
#     "pydantic>=2.11.7",
#     "python-dotenv>=1.2.1",
#     "requests>=2.32.5",
#     "youtube-transcript-api>=1.2.3",
# ]
# ///

from mcp.server.fastmcp import FastMCP # pyright: ignore[reportMissingImports]
from src.service import YouTubeTranscriptService
from src.files import FileService
from src.web_search import WebSearchService
from dotenv import load_dotenv
import os

load_dotenv()

mcp = FastMCP(
    name="YouTube",
    stateless_http=True,
)

_service = YouTubeTranscriptService(use_proxy=True)
_file_service = FileService(os.getenv("ALLOWED_DIRECTORY"))
_search_service = WebSearchService()


@mcp.tool()
def get_transcript(
    video_url_or_id: str,
) -> str:
    """Get transcript as plain text."""
    try:
        return _service.get_transcript_text(video_url_or_id)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def list_files(sub_dir: str = "") -> str:
    """List files in the allowed storage directory."""
    try:
        files = _file_service.list_files(sub_dir)
        return "\n".join(files) if files else "No files found."
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def read_file(file_path: str) -> str:
    """Read a file from the allowed storage directory."""
    try:
        return _file_service.read_file(file_path)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def write_file(file_path: str, content: str) -> str:
    """Write content to a file in the allowed storage directory."""
    try:
        return _file_service.write_file(file_path, content)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def search_web(query: str, max_results: int = 5) -> str:
    """Perform a web search for the given query."""
    try:
        results = _search_service.search(query, max_results=max_results)
        return _search_service.format_results(results)
    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    mcp.run(transport="stdio")