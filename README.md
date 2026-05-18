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

