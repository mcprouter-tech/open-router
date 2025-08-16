#!/bin/bash

echo -e "\n📦 Setting up contextus.sh development environment...\n"

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "❌ uv is not installed. Please install it first:"
    echo "   curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi

echo "✅ Found uv"

# Check if we're in a virtual environment
if [[ "$VIRTUAL_ENV" != "" ]]; then
    echo "⚠️  You're already in a virtual environment: $VIRTUAL_ENV"
    echo "   This might cause conflicts. Consider deactivating first."
fi

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "🔧 Creating virtual environment..."
    uv venv
else
    echo "✅ Virtual environment already exists"
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source .venv/bin/activate

# Install dependencies
echo "📦 Installing dependencies..."
uv pip install -e ".[dev]"

# Check if installation was successful
if command -v contextus &> /dev/null; then
    echo "✅ Contextus installed successfully!"
    echo ""
    echo "🎉 Development environment ready!"
    echo ""
    echo "Try these commands:"
    echo "   contextus --help"
    echo "   contextus --version"
    echo ""
    echo "To run tests:"
    echo "   pytest"
    echo ""
    echo "To format code:"
    echo "   ruff format ."
    echo ""
    echo "To lint code:"
    echo "   ruff check ."
else
    echo "❌ Installation failed"
    exit 1
fi

# Check if we can import the package
echo "🧪 Testing import..."
python -c "import contextus; print(f'✅ Contextus {contextus.__version__} imported successfully')" || {
    echo "❌ Failed to import contextus package"
    exit 1
}

echo ""
echo "🚀 Ready to develop! The virtual environment is activated."
echo "   To deactivate later, run: deactivate"
