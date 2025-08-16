#!/usr/bin/env python3
"""
Test script for Contextus CLI
Run this script directly to test the CLI without installation
"""

import os
import sys

# Add the src directory to the path so we can import contextus
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))
from contextus.cli import main

if __name__ == "__main__":
    # Run the CLI with any command line arguments passed to this script
    sys.exit(main())
