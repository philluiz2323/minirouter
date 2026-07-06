"""Runtime helpers for coordinator build targets."""
from __future__ import annotations


def resolve_device_dtype(
    *,
    requested_device: str | None,
    requested_dtype: str | None,
    default_device: str,
    default_dtype: str,
    context: str,
) -> tuple[str, str]:
    """Resolve the coordinator device/dtype with a CPU fallback.

    If the caller requests a CUDA device but torch reports that CUDA is not
    available, the resolver falls back to ``cpu`` + ``float32``.
    """
    device = (requested_device or "").strip() or default_device
    dtype = (requested_dtype or "").strip() or default_dtype

    if str(device).startswith("cuda"):
        import torch

        if not torch.cuda.is_available():
            print(f"[{context}] CUDA unavailable; falling back to cpu/float32")
            return "cpu", "float32"

    if str(device) == "cpu":
        dtype_key = str(dtype).lower()
        if dtype_key not in {"float32", "fp32", "float"}:
            print(f"[{context}] forcing float32 on CPU (requested dtype={dtype!r})")
            dtype = "float32"

    return str(device), str(dtype)
