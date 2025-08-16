"""
Contextus Client package

Provides client-specific implementations and configuration
"""

from contextus.clients.base import BaseClientManager
from contextus.clients.client_config import ClientConfigManager
from contextus.clients.client_registry import ClientRegistry
from contextus.clients.managers.claude_desktop import ClaudeDesktopManager
from contextus.clients.managers.cursor import CursorManager
from contextus.clients.managers.trae import TraeManager
from contextus.clients.managers.windsurf import WindsurfManager

__all__ = [
    "BaseClientManager",
    "ClaudeDesktopManager",
    "WindsurfManager",
    "CursorManager",
    "TraeManager",
    "ClientConfigManager",
    "ClientRegistry",
]
