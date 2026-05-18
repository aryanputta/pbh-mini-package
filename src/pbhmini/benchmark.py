"""Benchmark helpers for the PBH mini package."""

from __future__ import annotations

import math

import numpy as np

from .abundance import abundance_curve
from .evaporation import ALPHA_G3_PER_S, lifetime_seconds, mass_at_time


def abundance_reference(amplitude: float, mass_solar: np.ndarray, delta_c: float = 0.45) -> np.ndarray:
    variance = np.full_like(mass_solar, (4.0 / 9.0) ** 2 * amplitude)
    erfc_vec = np.vectorize(math.erfc)
    beta = 0.5 * erfc_vec(delta_c / np.sqrt(2.0 * variance))
    return 2.7e8 * beta * mass_solar**-0.5


def abundance_benchmark(amplitude: float = 0.015, width: float = 0.5) -> dict[str, np.ndarray]:
    curve = abundance_curve(amplitude, width)
    reference = abundance_reference(amplitude, curve["mass_solar"])
    ratio = np.divide(curve["f_pbh"], reference, out=np.zeros_like(curve["f_pbh"]), where=reference > 0)
    return {"mass_solar": curve["mass_solar"], "toy_f_pbh": curve["f_pbh"], "reference_f_pbh": reference, "ratio": ratio}


def evaporation_benchmark(initial_mass_g: float = 1e10) -> dict[str, np.ndarray]:
    time = np.linspace(0.0, lifetime_seconds(initial_mass_g), 180)
    model = mass_at_time(initial_mass_g, time)
    remaining = initial_mass_g**3 - 3.0 * ALPHA_G3_PER_S * time
    reference = np.where(remaining > 0, np.cbrt(remaining), 0.0)
    return {"time_s": time, "model_mass_g": model, "reference_mass_g": reference, "abs_error_g": np.abs(model - reference)}

