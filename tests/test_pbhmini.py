from pathlib import Path

import numpy as np

from pbhmini import (
    abundance_benchmark,
    abundance_curve,
    baryon_asymmetry,
    evaporation_benchmark,
    lifetime_seconds,
    scan_parameters,
    write_evaporation_html,
)


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


def test_benchmark_outputs_are_finite():
    abundance = abundance_benchmark()
    evaporation = evaporation_benchmark()
    assert np.all(np.isfinite(abundance["ratio"]))
    assert evaporation["abs_error_g"].max() < 1e-6


def test_live_simulation_html_is_written(tmp_path):
    path = write_evaporation_html(Path(tmp_path) / "sim.html")
    assert path.exists()
    assert "PBH Evaporation Toy Simulation" in path.read_text(encoding="utf-8")
