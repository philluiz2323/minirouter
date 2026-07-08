"""Reproducibility tests for the sep-CMA-ES seed handling.

pycma treats ``seed == 0`` as "unseeded" and does NOT fix numpy's RNG, so a run
started with the default ``seed=0`` was silently non-reproducible even though the
API documents the seed as reproducible. These tests lock the remap: ``seed=0`` is
now deterministic, distinct seeds still differ, and nonzero seeds are unchanged.

``cma`` is a hard dependency of the project, but skip gracefully if it is not
installed on the box running the tests (matches the repo's offline-friendly stance).
"""
from __future__ import annotations

import numpy as np
import pytest

pytest.importorskip("cma")

from trinity.optim.sep_cmaes import SepCMAES, effective_seed  # noqa: E402


def _first_population(seed: int) -> np.ndarray:
    es = SepCMAES(n=32, sigma0=0.1, seed=seed, maxiter=5)
    return np.asarray(es.ask())


def test_effective_seed_maps_zero_to_nonzero():
    assert effective_seed(0) != 0
    # Every nonzero seed is passed through unchanged.
    for s in (1, 7, 42, 2**31):
        assert effective_seed(s) == s


def test_seed_zero_is_reproducible():
    # The regression: two seed=0 optimizers must now agree (pycma used to ignore 0).
    a = _first_population(0)
    b = _first_population(0)
    assert np.allclose(a, b)


def test_distinct_seeds_differ():
    assert not np.allclose(_first_population(7), _first_population(9))
    # seed=0 must not collide with the remap target's originating seed space in a
    # way that makes two conceptually-different seeds identical to seed 1.
    assert not np.allclose(_first_population(0), _first_population(1))


def test_nonzero_seed_reproducible():
    assert np.allclose(_first_population(7), _first_population(7))
