"""Async helpers for bounded fan-out."""
from __future__ import annotations

import asyncio
from collections.abc import Iterable
from typing import Any


async def gather_in_batches(
    awaitables: Iterable[Any],
    *,
    batch_size: int,
    return_exceptions: bool = False,
) -> list[Any]:
    """Run awaitables in bounded batches and preserve order.

    This is used for large benchmark sweeps so we do not launch hundreds of
    trajectories at once.
    """
    items = list(awaitables)
    if not items:
        return []
    size = max(1, int(batch_size))
    results: list[Any] = []
    for start in range(0, len(items), size):
        batch = items[start : start + size]
        results.extend(await asyncio.gather(*batch, return_exceptions=return_exceptions))
    return results
