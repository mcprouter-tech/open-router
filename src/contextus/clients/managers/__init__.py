"""
Client manager implementations for various MCP clients

This package contains specific implementations of client managers for MCP clients.
"""

from contextus.clients.managers.claude_desktop import ClaudeDesktopManager
from contextus.clients.managers.cline import ClineManager
from contextus.clients.managers.continue_extension import ContinueManager
from contextus.clients.managers.cursor import CursorManager
from contextus.clients.managers.fiveire import FiveireManager
from contextus.clients.managers.goose import GooseClientManager
from contextus.clients.managers.trae import TraeManager
from contextus.clients.managers.windsurf import WindsurfManager

__all__ = [
    "ClaudeDesktopManager",
    "CursorManager",
    "WindsurfManager",
    "ClineManager",
    "ContinueManager",
    "FiveireManager",
    "GooseClientManager",
    "TraeManager",
]
