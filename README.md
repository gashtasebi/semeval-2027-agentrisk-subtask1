# semeval-2027-agentrisk-subtask1
Research, experiments, and reproducible baselines for SemEval-2027 Task 10 AgentRisk Subtask 1: Risk Level Estimation.

# Researcher Team (DefenceGru-hhu):
- Abed.G
- Chaima.D



# SemEval 2027 — AgentRisk Subtask 1

## Project Overview

This repository documents the research, implementation, and
evaluation of a system for SemEval 2027 Task 10:
Risk Understanding in Agentic Systems.

**Focus:** Subtask 1 — Risk Level Estimation

The objective is to estimate the risk severity of a proposed
agent action given the preceding interaction trajectory.

## Research Questions

- RQ1: How accurately can models estimate risk severity?
- RQ2: Does the full interaction trajectory improve prediction
  compared with the proposed action alone?
- RQ3: Which types of examples lead to the largest prediction errors?
- RQ4: Can an ordinal-aware approach improve the official evaluation
  metric compared with simple baselines?

These questions are provisional and may be refined after reviewing
the official task guidelines and dataset.

## Repository Structure

- `RESEARCH_PLAN.md`: research objectives and milestones
- `RESEARCH_LOG.md`: chronological research diary
- `DECISION_LOG.md`: rationale for methodological decisions
- `EXPERIMENTS.md`: experiment registry
- `docs/`: task, dataset, literature, and evaluation documentation
- `notebooks/`: exploratory data analysis
- `src/`: reusable implementation
- `configs/`: experiment configurations
- `tests/`: reproducibility and correctness tests
- `results/`: generated tables and figures
- `reports/weekly/`: weekly progress reports

## Current Status

**Phase:** Repository setup and task verification

No experimental results are reported until the corresponding
experiments have been executed and documented.

## Reproducibility

Every reported experiment should specify:

- Dataset version or revision
- Data split
- Model and configuration
- Random seed, where applicable
- Evaluation metric
- Code commit
- Results and known limitations

## Data and Ethics

Dataset files are not redistributed in this repository unless
their license and the competition rules explicitly permit it.

API keys, credentials, and private data must never be committed.

