#!/usr/bin/env bash
# Run a trinity command on the remote GPU box, pinned to GPU 5.
# Usage (from local): bash scripts/run_remote.sh train --config configs/trinity.yaml
#                     bash scripts/run_remote.sh eval  --config configs/benchmarks.yaml
set -euo pipefail

HOST="${TRINITY_GPU_HOST:-trinity-gpu}"
REMOTE_DIR="${TRINITY_REMOTE_DIR:-trinity}"

CMD="$1"; shift
ssh "$HOST" \
  "cd $REMOTE_DIR && source .venv/bin/activate && \
   source scripts/remote_env.sh && \
   python -m trinity.$CMD $*"
