from __future__ import annotations

import csv
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from pbhmini import abundance_curve, abundance_history, baryon_asymmetry, scan_parameters


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

    history = abundance_history(1e10, 1.0, remnant_mass_g=1e5)
    eta = baryon_asymmetry(1e9, 1e12, 1e-25, 1e-9)
    print(f"final_relative_fraction={history['relative_fraction'][-1]:.6e}")
    print(f"toy_eta_b={eta:.6e}")


if __name__ == "__main__":
    main()
