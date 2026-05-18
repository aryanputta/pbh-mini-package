"""Parameter scan helpers."""

from __future__ import annotations

import numpy as np

from .abundance import abundance_curve


def scan_parameters(
    amplitudes: np.ndarray,
    widths: np.ndarray,
    limit: float = 1e-2,
) -> list[dict[str, float | bool]]:
    rows: list[dict[str, float | bool]] = []
    for amplitude in amplitudes:
        for width in widths:
            curve = abundance_curve(float(amplitude), float(width))
            peak = float(curve["f_pbh"].max())
            rows.append(
                {
                    "amplitude": float(amplitude),
                    "width": float(width),
                    "peak_f_pbh": peak,
                    "allowed": peak <= limit,
                }
            )
    return rows

