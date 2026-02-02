from ddgs import DDGS # pyright: ignore[reportMissingImports]
from typing import List, Dict

class WebSearchService:
    """Service for performing web searches using DuckDuckGo."""
    
    def __init__(self):
        self.ddgs = DDGS()

    def search(self, query: str, max_results: int = 5) -> List[Dict[str, str]]:
        """Perform a web search and return results."""
        results = []
        # ddgs.text returns a generator of dicts: {'title', 'href', 'body'}
        for r in self.ddgs.text(query, max_results=max_results):
            results.append({
                "title": r.get("title", ""),
                "url": r.get("href", ""),
                "snippet": r.get("body", "")
            })
        return results

    def format_results(self, results: List[Dict[str, str]]) -> str:
        """Format search results into a readable string."""
        if not results:
            return "No results found."
        
        formatted = []
        for i, r in enumerate(results, 1):
            formatted.append(f"{i}. {r['title']}\n   URL: {r['url']}\n   Snippet: {r['snippet']}\n")
        
        return "\n".join(formatted)
