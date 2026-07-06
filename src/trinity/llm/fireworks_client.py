"""Fireworks compatibility wrapper for the shared OpenAI-compatible pool."""
from __future__ import annotations

from .openai_compatible_pool import ChatResult, OpenAICompatiblePool, main

FireworksPool = OpenAICompatiblePool

__all__ = ["ChatResult", "OpenAICompatiblePool", "FireworksPool", "main"]


if __name__ == "__main__":
    main()
