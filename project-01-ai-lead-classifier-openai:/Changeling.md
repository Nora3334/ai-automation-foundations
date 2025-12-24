# Changelog

All notable changes to this project are documented in this file.

This project follows **Semantic Versioning**:

`MAJOR.MINOR.PATCH`

* **MAJOR**: Breaking architectural or API changes
* **MINOR**: New features, backward compatible
* **PATCH**: Bug fixes, refactors, documentation

---

## [1.0.0] – Portfolio Release (Real AI)

**Status:** Current

### Added

* Integrated real OpenAI API for lead classification
* Secure API key handling using `.env`
* AI prompt structured for deterministic JSON output
* Dual output support: JSON + CSV
* Production-style folder structure (`src`, `data`, `docs`)
* Detailed README with business + technical explanation

### Changed

* Replaced mock AI logic with real LLM-based classification
* Refactored `main.py` to act as orchestration layer
* Improved error handling and logging clarity

### Notes

This version represents a **portfolio-ready, end-to-end AI automation project** suitable for demonstrations, freelancing, and interviews.

---

## [0.2.0] – Mock AI + Workflow Validation

### Added

* Mock AI classifier to simulate LLM behavior
* CSV input parsing and preprocessing
* JSON output generation
* Modular file separation (pre, AI, post processing)

### Purpose

Validate workflow design and automation logic before using a paid AI API.

---

## [0.1.0] – Initial Foundation

### Added

* Basic Python scripts for CSV ingestion
* Dictionary-based lead processing
* Local file-based testing

### Purpose

Learning-oriented prototype used to understand Python, data handling, and automation fundamentals.

---

## Planned

* [ ] Add unit tests
* [ ] Add FastAPI wrapper for API-based usage
* [ ] Add async processing for larger CSV files
* [ ] Add confidence scoring per classification

---

*Last updated: 2025*
