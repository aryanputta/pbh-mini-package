"""Toy Hawking evaporation helpers."""

from __future__ import annotations

import numpy as np

AGE_UNIVERSE_S = 4.35e17
ALPHA_G3_PER_S = (5.0e14) ** 3 / (3.0 * AGE_UNIVERSE_S)


def lifetime_seconds(initial_mass_g: float, remnant_mass_g: float = 0.0) -> float:
    if initial_mass_g <= 0:
        raise ValueError("initial_mass_g must be positive")
    if remnant_mass_g < 0 or remnant_mass_g >= initial_mass_g:
        raise ValueError("invalid remnant mass")
    return (initial_mass_g**3 - remnant_mass_g**3) / (3.0 * ALPHA_G3_PER_S)


def mass_at_time(initial_mass_g: float, time_s: np.ndarray, remnant_mass_g: float = 0.0) -> np.ndarray:
    remaining = initial_mass_g**3 - 3.0 * ALPHA_G3_PER_S * np.asarray(time_s)
    floor = remnant_mass_g**3 if remnant_mass_g else 0.0
    mass = np.cbrt(np.maximum(remaining, floor))
    return np.where(remaining > 0, mass, remnant_mass_g)


def abundance_history(initial_mass_g: float, initial_fraction: float, remnant_mass_g: float = 0.0) -> dict[str, np.ndarray]:
    end = min(AGE_UNIVERSE_S, 1.2 * lifetime_seconds(initial_mass_g, remnant_mass_g))
    time = np.linspace(0.0, end, 180)
    mass = mass_at_time(initial_mass_g, time, remnant_mass_g)
    return {"time_s": time, "mass_g": mass, "relative_fraction": initial_fraction * mass / initial_mass_g}

