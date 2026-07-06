"""Chutes client for the coordinated LLM pool."""
from __future__ import annotations

from pathlib import Path

from .openai_compatible_pool import OpenAICompatiblePool

_REPO_ROOT = Path(__file__).resolve().parents[3]
_DEFAULT_CONFIG = _REPO_ROOT / "configs" / "models.chutes.yaml"


class ChutesPool(OpenAICompatiblePool):
    """Chutes-backed pool using the same chat-completions interface."""

    def __init__(self, config_path: str | Path = _DEFAULT_CONFIG):
        super().__init__(config_path)
