"""Toy baryogenesis estimate from PBH evaporation products."""

GEV_PER_GRAM = 5.60958885e23


def baryon_asymmetry(
    pbh_mass_g: float,
    heavy_mass_gev: float,
    pbh_yield: float,
    epsilon_cp: float,
    energy_fraction: float = 0.01,
    dilution: float = 1.0,
) -> float:
    if pbh_mass_g <= 0 or heavy_mass_gev <= 0:
        raise ValueError("masses must be positive")
    emitted = energy_fraction * pbh_mass_g * GEV_PER_GRAM / heavy_mass_gev
    return dilution * epsilon_cp * emitted * pbh_yield

