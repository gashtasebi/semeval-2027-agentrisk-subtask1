# Research Log — AgentRisk Subtask 1

## Project Overview

**Task:** SemEval 2027 Task 10 — AgentRisk
**Subtask:** 1 — Risk Level Estimation
**Start date:** 2026-10-23

The goal of this project is to estimate the risk severity of a proposed action in the context of a preceding agent interaction. The target is `risk_severity`, with values from 1 to 5. The main evaluation metric is Mean Absolute Error (MAE).

This log records the work completed so far, the main results, and the next steps.

## Current Status

**Last updated:** 2026-10-24

- The project repository and research documentation have been created.
- The train and dev datasets have passed the initial structural checks.
- The official split manifest has been checked, with no example ID overlap or scenario-group overlap between train and dev.
- Two constant-prediction baselines have been evaluated.
- The distribution of risk labels has been analyzed.
- The next step is to test a simple method that uses the interaction text and proposed action.

## Entry 001 — Project Setup

**Date:** 2026-10-23

### Work completed
- Created the project repository and basic folder structure.
- Added initial research planning and documentation files.
- Set up Git for version control and started keeping a research log.

### Outcome
The project has a basic structure for documenting experiments, tracking code changes, and recording results.

## Entry 002 — Task and Dataset Review

**Date:** 2026-10-24

### Work completed
- Reviewed the AgentRisk dataset documentation on Hugging Face.
- Identified the target field, relevant input fields, dataset splits, and evaluation metric.
- Recorded the task description in `docs/task_description.md`.

### Main findings
- The target field is `risk_severity`, with integer labels from 1 to 5.
- The relevant input fields include `formatted_interaction` and `proposed_action`.
- The dataset contains 568 training examples and 143 dev examples.
- The primary metric for Subtask 1 is MAE.
- The split manifest records example IDs, split assignments, and scenario groups.

### Limitation
This review was based on the dataset documentation. The local files and split assignments were checked separately in the following steps.

## Entry 003 — Dataset Validation

**Date:** 2026-10-24

### Work completed
- Created and ran `src/validate_dataset.py`.
- Checked JSONL parsing, required fields, risk label values, and duplicate IDs within each split.

### Results

| Check | Train | Dev |
|---|---:|---:|
| Records | 568 | 143 |
| JSON parsing errors | 0 | 0 |
| Missing required fields | 0 | 0 |
| Invalid risk labels | 0 | 0 |
| Duplicate IDs within split | 0 | 0 |

### Outcome
Both files passed the initial structural checks. No invalid labels or duplicate IDs within either split were found.

## Entry 004 — Split and Scenario-Group Validation

**Date:** 2026-10-24

### Work completed
- Created and ran `src/validate_splits.py`.
- Compared the train and dev files with `data/metadata/split_manifest.jsonl`.
- Checked split assignments, duplicate manifest IDs, missing IDs, and scenario-group overlap.

### Results
- Manifest records: 711
- Unique manifest IDs: 711
- Train examples: 568
- Dev examples: 143
- Split assignment mismatches: 0
- Manifest IDs absent from train/dev: 0
- Train scenario groups: 302
- Dev scenario groups: 95
- Scenario groups shared between train and dev: 0

### Outcome
The downloaded train and dev files matched the split manifest. No example ID overlap or scenario-group overlap was found between the two splits.

This check supports the integrity of the provided split, but it does not rule out every possible form of data leakage.

## Entry 005 — Median Baseline

**Date:** 2026-10-24

### Objective
Get a first reference score before testing more complex methods.

### Method
- Created `src/agentrisk/baseline_median.py`.
- Calculated the median `risk_severity` in the training set.
- Used that value as the prediction for every dev example.
- Evaluated the predictions using MAE.

### Results
- Train examples: 568
- Dev examples: 143
- Median training label: 2
- Dev MAE: 1.216783
- Automated tests: 4 passed

### Interpretation
The model predicts risk level 2 for every dev example. The MAE of 1.216783 is the first reference score for later comparisons.

### Limitation
This baseline does not use the interaction text or proposed action.

## Entry 006 — Mean Baseline

**Date:** 2026-10-24

### Objective
Compare a constant mean prediction with the median baseline.

### Method
- Created `src/agentrisk/baseline_mean.py`.
- Calculated the mean `risk_severity` in the training set.
- Used that value as a constant prediction for every dev example.
- Evaluated the predictions using MAE.

### Results
- Train examples: 568
- Dev examples: 143
- Mean training label: 2.272887
- Dev MAE: 1.226325

### Interpretation
The mean baseline had a slightly higher MAE than the median baseline on the same dev set. The median baseline is therefore the stronger of these two reference methods so far.

### Limitation
Like the median baseline, this method does not use the interaction text or proposed action.

## Entry 007 — Risk Label Distribution

**Date:** 2026-10-24

### Objective
Check how the five risk levels are distributed in the train and dev sets.

### Method
- Created and ran `src/agentrisk/analyze_labels.py`.
- Counted examples for each label and calculated their percentages.

### Results

| Risk level | Train count | Train percentage | Dev count | Dev percentage |
|---:|---:|---:|---:|---:|
| 1 | 265 | 46.65% | 66 | 46.15% |
| 2 | 33 | 5.81% | 8 | 5.59% |
| 3 | 127 | 22.36% | 32 | 22.38% |
| 4 | 136 | 23.94% | 35 | 24.48% |
| 5 | 7 | 1.23% | 2 | 1.40% |

### Interpretation
The label distribution is uneven. Risk level 1 is the most common, while risk level 5 has very few examples. The train and dev distributions are similar, but the small number of level 5 examples means that results for this level may be difficult to assess reliably.

### Limitation
This analysis describes label counts only. It does not explain why examples received their labels or measure model performance for each level.

## Current Results Summary

| Method | Uses interaction text? | Dev MAE |
|---|---|---:|
| Constant median | No | 1.216783 |
| Constant mean | No | 1.226325 |

The median baseline currently has the lower MAE. Neither baseline uses the interaction text or proposed action, so the next experiments should test whether using these inputs improves performance.

## Next Steps

1. Review the evaluation protocol and confirm any remaining submission requirements.
2. Develop a simple baseline that uses the interaction text and proposed action.
3. Evaluate it on the same official dev split using MAE.
4. Compare the result with the median and mean baselines.
5. Inspect errors across risk levels, keeping the small number of level 5 examples in mind.
6. Record the code, configuration, and results for each new experiment.

## Dataset Source

AgentRisk dataset repository:
https://huggingface.co/datasets/AgentRisk/agentrisk-data-2027
