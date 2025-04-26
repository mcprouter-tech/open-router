
# 🌟 MCPRouter - Model Context Protocol Router

MCPRouter is an open source service and a CLI package management tool for MCP servers. It simplifies managing server configurations across various supported clients, allows grouping servers into profiles, helps discover new servers via a registry, and includes a powerful router that aggregates multiple MCP servers behind a single endpoint with shared sessions.


## 🤝 Community Contributions

> 💡 **Grow the MCP ecosystem!** We welcome contributions to our [MCP Registry](mcp-registry/README.md). Add your own servers, improve documentation, or suggest features. Open source thrives with community participation!

## 🚀 Quick Installation

Choose your preferred installation method:

### 🍺 Homebrew

```bash
brew install MCPRouter
```

### 📦 pipx (Recommended for Python tools)

```bash
pipx install MCPRouter
```

### 🐍 pip

```bash
pip install MCPRouter
```


## 🔎 Overview

MCPRouter simplifies the installation, configuration, and management of Model Context Protocol servers and their configurations across different applications (clients). Key features include:

- ✨ Easy addition and removal of MCP server configurations for supported clients.
- 📋 Centralized management using profiles: group server configurations together and activate/deactivate them easily.
- 🔍 Discovery of available MCP servers through a central registry.
- 🔌 MCPM Router for aggregating multiple MCP servers behind a single endpoint with shared sessions.
- 💻 A command-line interface (CLI) for all management tasks.

See [Advanced Features](docs/advanced_features.md) for more capabilities like shared server sessions and the MCPM Router.

## 🖥️ Supported MCP Clients

MCPRouter will support managing MCP servers for the following clients:

- 🤖 Claude Desktop (Anthropic)
- ⌨️ Cursor
- 🏄 Windsurf
- 📝 Cline
- ➡️ Continue
- 🦢 Goose
- 🔥 5ire
- 🦘 Roo Code
- ✨ More clients coming soon...

## 🔥 Command Line Interface (CLI)

MCPRouter provides a comprehensive CLI built with Python's Click framework. Commands generally operate on the currently **active client**. You can view/set the active client using `mcpm client`. Many commands also support scope modifiers like `@CLIENT_NAME/SERVER_NAME` or `#PROFILE_NAME/SERVER_NAME` to target specific clients or profiles directly.

Below are the available commands, grouped by functionality:

