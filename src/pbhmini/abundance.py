"""Toy PBH abundance calculations."""

from __future__ import annotations

import math

import numpy as np

K_REF_MPC = 2.9e5


def curvature_power(k: np.ndarray, amplitude: float, k0: float, width: float) -> np.ndarray:
    if amplitude <= 0 or k0 <= 0 or width <= 0:
        raise ValueError("amplitude, k0, and width must be positive")
    return amplitude * np.exp(-0.5 * (np.log(k / k0) / width) ** 2)


def horizon_mass_solar(k: np.ndarray) -> np.ndarray:
    return 30.0 * (k / K_REF_MPC) ** -2


def collapse_fraction(variance: np.ndarray, delta_c: float = 0.45) -> np.ndarray:
    erfc_vec = np.vectorize(math.erfc)
    return 0.5 * erfc_vec(delta_c / np.sqrt(2.0 * variance))


def abundance_curve(amplitude: float, width: float, k0: float = K_REF_MPC) -> dict[str, np.ndarray]:
    k = np.geomspace(k0 / 50.0, k0 * 50.0, 140)
    mass = horizon_mass_solar(k)
    variance = (4.0 / 9.0) ** 2 * curvature_power(k, amplitude, k0, width)
    beta = collapse_fraction(np.maximum(variance, 1e-300))
    f_pbh = 2.7e8 * beta * mass ** -0.5
    order = np.argsort(mass)
    return {"mass_solar": mass[order], "beta": beta[order], "f_pbh": f_pbh[order]}

