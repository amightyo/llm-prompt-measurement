# LLM Prompt-Induced Measurement Variability

This repository contains the reproducible research workflow for an empirical study examining prompt-induced measurement variability in large language
model (LLM)-based educational essay scoring.

## Study Purpose

The study investigates whether LLM-generated essay scores vary as a function of prompt specification and whether such variability represents a meaningful source of measurement error.

The study is situated within educational measurement and uses Generalizability Theory as a framework for examining multiple sources of score variation.

## Research Questions

1. To what extent does AI-human agreement in essay scoring differ across prompting strategies?

2. To what extent does within-model scoring reliability differ across prompting strategies?

3. Does prompt-induced scoring variability differ across levels of student writing performance?

## Proposed Design

Student essays are evaluated under three LLM prompting conditions:

1. Minimal scoring prompt
2. Rubric-informed prompt
3. Rubric plus anchor-response prompt

Each essay is evaluated repeatedly under each condition to distinguish prompt-related variability from run-to-run model variability.

## Repository Structure

- `data/raw/` — original source data, excluded from Git
- `data/processed/` — cleaned and analytic datasets
- `src/` — Python analysis scripts
- `outputs/tables/` — generated manuscript tables
- `outputs/figures/` — generated manuscript figures
- `paper/` — Quarto manuscript and bibliography
- `docs/` — research protocols and methodological documentation

## Reproducibility

Analyses are conducted in Python and the manuscript is produced using Quarto.
Tables and figures are generated programmatically wherever possible.

## Status

Study in progress.