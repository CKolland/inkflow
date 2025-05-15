"""
This is the initialization file for the inkflow package.
It may include package-level documentation or import statements for public classes and functions.
"""

from .cli import main as cli  # Import the CLI entry point for public use

__all__ = ["cli"]  # Public API of the package
