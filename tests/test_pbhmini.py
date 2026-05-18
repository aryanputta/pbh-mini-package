import numpy as np

from pbhmini import abundance_curve, baryon_asymmetry, lifetime_seconds, scan_parameters


def test_abundance_increases_with_amplitude():
    low = abundance_curve(0.008, 0.5)["f_pbh"].max()
    high = abundance_curve(0.015, 0.5)["f_pbh"].max()
    assert high > low


def test_scan_parameters_shape():
    rows = scan_parameters(np.array([0.008, 0.015]), np.array([0.3, 0.7]))
    assert len(rows) == 4
    assert {"amplitude", "width", "peak_f_pbh", "allowed"} == set(rows[0])


def test_lifetime_mass_scaling():
    assert lifetime_seconds(2e10) > lifetime_seconds(1e10)


def test_baryon_asymmetry_positive():
    assert baryon_asymmetry(1e9, 1e12, 1e-25, 1e-9) > 0

