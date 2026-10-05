# DRAM Sacrificial Capacitor Mold Removal

**ChipFoundryServices Technical Series · First edition · Version 1.0.0.0 · 2026-10-05**

A technical e-book about releasing DRAM storage-node electrodes from their sacrificial mold while preserving the supports, bottom stop, electrode surface, and mechanical stability needed for capacitor formation.

Read [the preface](PREFACE.md), browse [the complete index](INDEX.md), or start with [Chapter 1](chapters/01-release-module.md). Download the [single-volume Markdown e-book](dist/dram-sacrificial-capacitor-mold-removal.md) or [HTML e-book](dist/dram-sacrificial-capacitor-mold-removal.html). Download the HTML file and open it locally for formatted reading and printing; GitHub's file view displays its source.

## Scope and structure

The book follows the sibling series pattern: **16 chapters in four parts, seven appendices, and a glossary**. It concentrates on the release process after support access, with chapters on chemistry, moving fronts, wet hardware, vapor-HF compatibility, rinse and drying, support survival, electrode interfaces, residual mold, statistics, alternative molds, qualification, and economics.

[DRAM Capacitor Mold Etch](https://github.com/chipfoundryservices/dram-capacitor-mold-etch) supplies the broader support-open/mold-removal context. [DRAM Capacitor Support Layer Etch](https://github.com/chipfoundryservices/dram-capacitor-support-layer-etch) covers the dedicated support-patterning operation. This volume is original release-focused content; it does not duplicate those chapters or claim a new numbered series slot.

## Evidence and numerical examples

[References](REFERENCES.md) map narrow technical claims to primary publications and patent disclosures. [Research notes](research/RESEARCH.md) document the repositories reviewed, scope, corrections, and evidence gaps. All rates, modulus values, economic inputs, and acceptance thresholds in worked examples are explicitly illustrative unless attributed. Patent disclosures describe proposed implementations and are not proof of production adoption.

The reference geometry uses 45 nm triangular pitch, a constant 28 nm pillar diameter, and 1.60 µm overall height. Calculations account for the 1580 nm mold/support stack plus a separate 20 nm bottom stop. The [assumption register](appendices/A-material-properties.md) defines the model boundaries.

## Build and validate

Python 3.11 or newer is supported. Install the small build dependency in an isolated environment:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python scripts/calculations.py
.venv/bin/python scripts/validate.py
.venv/bin/python scripts/build.py
.venv/bin/python scripts/validate.py --dist
```

The build produces portable, self-contained HTML and one-volume Markdown in `dist/`. Internal book links resolve within each compiled volume. GitHub Actions repeats calculation, link, and build checks and uploads the e-book files as an artifact. No credentials are needed to read or build the book.

This is an educational engineering reference, with qualification workflows rather than a transferable fabrication recipe. Manufacturing decisions require measurements on the actual stack and equipment.
