import warnings

from contextus.core.schema import RemoteServerConfig, ServerConfig, STDIOServerConfig

__all__ = ["ServerConfig", "RemoteServerConfig", "STDIOServerConfig", "RemoteServerConfig"]

warnings.warn("contextus.schemas.server_config is deprecated, use contextus.core.schema instead", DeprecationWarning)
