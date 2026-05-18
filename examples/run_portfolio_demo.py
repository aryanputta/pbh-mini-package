from __future__ import annotations

import csv
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from pbhmini import (
    abundance_benchmark,
    abundance_curve,
    abundance_history,
    baryon_asymmetry,
    evaporation_benchmark,
    scan_parameters,
    write_evaporation_html,
)


def main() -> None:
    results_dir = Path("results")
    results_dir.mkdir(exist_ok=True)

    curve = abundance_curve(0.015, 0.5)
    fig, ax = plt.subplots(figsize=(7.0, 4.6))
    ax.loglog(curve["mass_solar"], np.maximum(curve["f_pbh"], 1e-300))
    ax.set_xlabel("PBH mass [$M_\\odot$]")
    ax.set_ylabel("Toy $f_{PBH}$")
    ax.set_title("Mini-package abundance example")
    ax.grid(True, which="both", alpha=0.3)
    fig.tight_layout()
    fig.savefig(results_dir / "example_abundance.png", dpi=180)
    plt.close(fig)

    rows = scan_parameters(np.linspace(0.006, 0.02, 8), np.linspace(0.2, 0.9, 6))
    with (results_dir / "example_scan.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    benchmark = abundance_benchmark()
    fig, axes = plt.subplots(2, 1, figsize=(7.0, 6.2), sharex=True)
    axes[0].loglog(benchmark["mass_solar"], np.maximum(benchmark["toy_f_pbh"], 1e-300), label="toy")
    axes[0].loglog(benchmark["mass_solar"], np.maximum(benchmark["reference_f_pbh"], 1e-300), "--", label="reference")
    axes[0].set_ylabel("$f_{PBH}$")
    axes[0].set_title("Mini-package benchmark comparison")
    axes[0].legend()
    axes[0].grid(True, which="both", alpha=0.3)
    axes[1].semilogx(benchmark["mass_solar"], benchmark["ratio"])
    axes[1].axhline(1.0, color="black", linestyle="--", linewidth=1.0)
    axes[1].set_xlabel("PBH mass [$M_\\odot$]")
    axes[1].set_ylabel("toy / reference")
    axes[1].grid(True, which="both", alpha=0.3)
    fig.tight_layout()
    fig.savefig(results_dir / "example_benchmark_compare.png", dpi=180)
    plt.close(fig)

    history = abundance_history(1e10, 1.0, remnant_mass_g=1e5)
    evap_bench = evaporation_benchmark()
    write_evaporation_html(results_dir / "live_evaporation_simulation.html")
    eta = baryon_asymmetry(1e9, 1e12, 1e-25, 1e-9)
    print(f"final_relative_fraction={history['relative_fraction'][-1]:.6e}")
    print(f"max_evaporation_benchmark_error_g={evap_bench['abs_error_g'].max():.6e}")
    print(f"toy_eta_b={eta:.6e}")


if __name__ == "__main__":
    main()
