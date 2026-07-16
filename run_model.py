#!/usr/bin/env python
"""
TINE Model Interface - Direct Python Launcher
Simple wrapper to run model interface commands
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.dirname(__file__))

from src.model_cli import main

if __name__ == "__main__":
    main()
