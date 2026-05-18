# PBH Mini Package

`pbh-mini-package` wraps the toy abundance, scan, evaporation, and baryogenesis
ideas into a small Python package with tests and an example script.

This repo is the polished portfolio version: simple modules, documented inputs,
reproducible example outputs, and clear limitations.

## Install And Run

```bash
pip install -e .
python examples/run_portfolio_demo.py
pytest
```

Outputs are written to `results/`.

Extra demo artifacts:

- `results/example_benchmark_compare.png`
- `results/live_evaporation_simulation.html`

The benchmark comparisons are analytic consistency checks. They are not
GRChombo or Einstein Toolkit validation runs.

## Scope

Included:

- lognormal curvature spectrum helper
- Gaussian-tail PBH abundance proxy
- parameter scan utilities
- Hawking evaporation remnant toy model
- baryogenesis bookkeeping estimate

Not included:

- full transfer functions
- non-Gaussian statistics
- critical collapse
- greybody spectra
- Boltzmann-equation washout
- observational constraint database
- numerical-relativity simulation through GRChombo or Einstein Toolkit

## External Simulation Benchmarks

GRChombo and Einstein Toolkit are large numerical-relativity frameworks that
need separate installation, problem setup, initial data, and compute resources.
This package provides clean comparison hooks and toy live visualizations first;
external simulation CSVs can be added later without changing the model code.
