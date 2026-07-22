# Study Design

## Study Focus

This study examines prompt-induced measurement variability in LLM-based educational essay scoring.

## Data Source

ASAP 2.0 automated essay scoring dataset.

## Selected Task

Facial Action Coding System.

Students were asked to construct an argument concerning the value of using facial-action recognition technology to interpret student emotions in classroom settings.

## Population

4,883 essays associated with the selected writing task.

## Analytic Sample

A stratified random sample of 180 essays was selected.

Thirty essays were randomly sampled from each human reference score level (1-6).

Sampling was conducted using a fixed random seed to ensure reproducibility.

## Experimental Design

Each essay will be scored under three prompting conditions:

1. Minimal prompt
2. Rubric-informed prompt
3. Rubric plus anchor essays

Each essay will be independently evaluated three times within each prompting condition.

Expected number of LLM ratings:

180 essays × 3 conditions × 3 replications = 1,620 ratings.

## Research Questions

RQ1. To what extent does agreement between LLM-generated and human reference scores differ across prompting strategies?

RQ2. To what extent does the reproducibility of LLM-generated essay scores differ across repeated evaluations and prompting strategies?

RQ3. To what extent does prompt-induced measurement variability differ across levels of student writing performance?

## Measurement Framework

The study conceptualizes prompt specification as a measurement facet within a Generalizability Theory framework.

Potential sources of score variation include:

- student essay performance;
- prompt specification;
- essay-by-prompt interaction;
- repeated LLM evaluation;
- residual variability.