import os
from pathlib import Path
from typing import List, Optional

class FileService:
    """Service for handling file operations within a restricted directory."""
    
    def __init__(self, base_dir: Optional[str] = None):
        # Default to a 'storage' folder in the project root if not specified
        if not base_dir:
            base_dir = os.path.join(os.getcwd(), "storage")
        
        self.base_dir = Path(base_dir).resolve()
        self._ensure_base_dir()

    def _ensure_base_dir(self):
        """Create the base directory if it doesn't exist."""
        self.base_dir.mkdir(parents=True, exist_ok=True)

    def _get_safe_path(self, relative_path: str) -> Path:
        """Resolve and validate that the path is within the base directory."""
        # Clean the path to prevent directory traversal
        target_path = (self.base_dir / relative_path).resolve()
        
        if not str(target_path).startswith(str(self.base_dir)):
            raise PermissionError(f"Access denied: {relative_path} is outside the allowed directory.")
        
        return target_path

    def list_files(self, sub_dir: str = "") -> List[str]:
        """List files in the allowed directory or a subdirectory."""
        path = self._get_safe_path(sub_dir)
        if not path.is_dir():
            raise NotADisdirectoryError(f"'{sub_dir}' is not a directory.")
        
        return [str(p.relative_to(self.base_dir)) for p in path.iterdir()]

    def read_file(self, file_path: str) -> str:
        """Read content of a file."""
        path = self._get_safe_path(file_path)
        if not path.is_file():
            raise FileNotFoundError(f"File not found: {file_path}")
        
        return path.read_text(encoding="utf-8")

    def write_file(self, file_path: str, content: str) -> str:
        """Write content to a file."""
        path = self._get_safe_path(file_path)
        # Ensure parent directories exist
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return f"Successfully wrote to {file_path}"
