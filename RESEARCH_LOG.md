# Research Log

## Entry 001 — Repository Initialization

**Date:** 2026-10-23  
**Research phase:** Project setup  
**Status:** In progress

### Objective
Establish a version-controlled and reproducible research workflow for
SemEval 2027 Task 10, AgentRisk, Subtask 1.

### Work performed
- Defined the repository structure.
- Created the initial research documentation.
- Established a plan for tracking experiments and weekly reports.

### Research questions
- What is the exact official prediction target?
- What are the dataset schema and official evaluation metric?
- What baseline methods are appropriate for this task?

### Results
No experiments have been conducted yet.

### Decisions
- Use Git for version control.
- Maintain a chronological research log.
- Record every experiment with its configuration and results.

### Problems and uncertainties
- Official task specifications and dataset details must be verified.
- The final experimental protocol has not yet been established.

### Next steps
1. Verify the official task instructions.
2. Inspect the dataset and its labels.
3. Implement a simple baseline.
4. Record the first quantitative results.

### Evidence
- Repository commit: [to be added]
- Relevant files: README.md, RESEARCH_PLAN.md

### Supervisor feedback
Pending.

## Entry 002 — Initial Dataset Documentation Review

**Date:** 2026-10-24
**Research phase:** Task specification and dataset documentation
**Status:** Initial documentation review completed; local data inspection pending

### Objective
Identify the dataset source and document the stated task definition,
prediction target, data splits, and primary evaluation metric for Subtask 1.

### Work performed
- Opened the AgentRisk dataset repository on Hugging Face.
- Inspected the dataset README provided at:
  https://huggingface.co/datasets/AgentRisk/agentrisk-data-2027
- Reviewed the documented fields, severity labels, data splits, and evaluation section.
- Updated `docs/task_description.md` to reflect the reviewed documentation.

### Findings from the dataset README
- Subtask 1 estimates the risk severity of executing the final proposed action
  in the context of the preceding interaction trajectory.
- The documented target field is `risk_severity`, with integer labels from 1 to 5.
- The documented input fields include `formatted_interaction` and `proposed_action`.
- The README reports 568 training examples and 143 development examples.
- The primary metric listed for Subtask 1 is Mean Absolute Error (MAE).
- The README describes `metadata/split_manifest.jsonl` as mapping example IDs
  to splits and scenario groups.
- The README states that examples derived from the same scenario are kept
  within the same split.

### Decisions
- Restrict the project to Subtask 1: Risk Level Estimation.
- Treat `risk_severity` as the prediction target.
- Do not treat dataset documentation alone as a substitute for the final
  official evaluation and submission instructions.
- Keep raw and processed local data out of version control.

### Limitations and open questions
- The dataset has not yet been downloaded or inspected locally.
- Schema, label distribution, missing values, and duplicate records have not
  been independently checked.
- The official evaluation and submission instructions still need review.
- No baseline has been implemented and no experiments have been run.

### Next steps
1. Inspect the available dataset files and loading instructions.
2. Download the relevant data locally using a reproducible method.
3. Validate the schema, labels, and split sizes.
4. Review the official evaluation instructions.
5. Establish a simple baseline and record its configuration and results.

### Evidence
- Dataset repository:
  https://huggingface.co/datasets/AgentRisk/agentrisk-data-2027
- Dataset README:
  https://huggingface.co/datasets/AgentRisk/agentrisk-data-2027/blob/main/README.md
- Related project file: `docs/task_description.md`
- Code commit: to be recorded after review and commit.

### Supervisor feedback
Pending.

## Entry 003 — Initial Dataset Validation

**Date:** 2026-10-24

### Objective
Validate the downloaded training and development JSONL files before conducting exploratory data analysis or modeling.

### Method
- Created `src/validate_dataset.py` using Python's standard library.
- Parsed both JSONL files and checked JSON parsing errors.
- Checked the presence of required Subtask 1 fields:
  `example_id`, `formatted_interaction`, `proposed_action`, and `risk_severity`.
- Checked that `risk_severity` is an integer from 1 to 5.
- Checked for duplicate example IDs within each split.

### Results

| Check | Train | Dev |
|---|---:|---:|
| Records | 568 | 143 |
| JSON parsing errors | 0 | 0 |
| Missing required fields | 0 | 0 |
| Invalid risk labels | 0 | 0 |
| Duplicate IDs within split | 0 | 0 |

Risk severity distribution:

| Label | Meaning | Train | Dev |
|---:|---|---:|---:|
| 1 | Minimal | 265 | 66 |
| 2 | Low | 33 | 8 |
| 3 | Moderate | 127 | 32 |
| 4 | High | 136 | 35 |
| 5 | Critical | 7 | 2 |

### Interpretation
Basic structural validation passed for both files. The label distribution is imbalanced, with relatively few Critical examples. This should be considered when establishing and interpreting baseline results.

### Limitations
- Duplicate IDs have only been checked within each split, not across train and dev.
- No scenario-group leakage analysis has been performed.
- No model has been trained, and no performance results are available.

### Next Steps
1. Check for ID overlap between train and dev.
2. Inspect the dataset schema and label distribution in more detail.
3. Establish a simple baseline and evaluate it using MAE.
## Entry 004 — Split and Scenario-Group Validation

**Date:** 2026-10-24

### Objective
Verify that the official split manifest matches the downloaded data and that scenario groups do not overlap between train and dev.

### Method
- Inspected `data/metadata/split_manifest.jsonl`.
- Created and ran `src/validate_splits.py`.
- Checked manifest JSON parsing, required fields, duplicate IDs, split assignments, and scenario-group overlap.

### Results
- Manifest records: 711; unique IDs: 711; duplicate IDs: 0.
- Train records: 568; dev records: 143.
- Train and dev IDs missing from the manifest: 0.
- Split assignment mismatches: 0.
- Manifest IDs absent from train/dev: 0.
- Train scenario groups: 302.
- Dev scenario groups: 95.
- Scenario groups shared between train and dev: 0.
- Unexpected split values: none.
- The validation script completed successfully.

### Interpretation
The downloaded train/dev files are consistent with the split manifest. No example-ID overlap or scenario-group overlap was found between the two splits. This supports the integrity of the provided split assignment, but does not rule out every possible form of data leakage.

### Next Steps
1. Review label distribution and establish a simple MAE baseline.
2. Keep the official split fixed for baseline evaluation.
3. Document modeling decisions and results before drawing conclusions.

## Entry 005 — First Baseline Experiment

**Date:** 2026-10-24

### Objective
Run a simple first experiment to get a reference score for Subtask 1.

### Work performed
- Created `src/agentrisk/baseline_median.py`.
- Used the median risk label in the training set as the prediction for every dev example.
- Calculated MAE on the official dev split.
- Added four automated tests for the MAE calculation.

### Results
- Training examples: 568
- Dev examples: 143
- Median training label: 2
- Dev MAE: 1.216783
- Automated tests: 4 passed

### What this means
The baseline predicts risk level 2 for every dev example. Its MAE is 1.216783, which gives us a starting point to compare with later models.

### Limitations
This is a very simple baseline. It does not use the interaction text or the proposed action, so it cannot make different predictions for different examples.

### Next steps
1. Keep this result as the reference for later experiments.
2. Try another simple baseline and compare its MAE on the same dev set.
3. Start testing a model that uses the interaction text.

## Entry 006 — Comparing Mean and Median Baselines

**Date:** 2026-10-24

### Objective
Compare two simple baselines for Subtask 1.

### Work performed
- Created `src/agentrisk/baseline_mean.py`.
- Used the mean training label as a constant prediction for every dev example.
- Compared the result with the median baseline.
- Ran the automated tests again.

### Results
- Training examples: 568
- Dev examples: 143
- Mean training label: 2.272887
- Mean baseline MAE: 1.226325
- Median baseline MAE: 1.216783
- Automated tests: 4 passed

### What this means
The median baseline had a slightly lower MAE than the mean baseline on the dev set. For now, the median baseline is our stronger reference result.

### Limitations
Neither baseline uses the interaction text or proposed action. Both make the same prediction for every dev example.

### Next steps
1. Keep both baseline results for future comparisons.
2. Check whether a simple text-based method can improve the MAE.
3. Continue using the official train and dev splits for evaluation.

## Entry 007 — Risk Label Distribution

**Date:** 2026-10-24

### Objective
Check how the five risk levels are distributed in the train and dev sets.

### Work performed
- Created `src/agentrisk/analyze_labels.py`.
- Counted the examples for each risk level.
- Calculated the percentage of each label in both splits.

### Results
- Train: 568 examples.
- Dev: 143 examples.
- Risk level 1 is the most common label in both splits, at about 46%.
- Risk level 2 accounts for about 6% of each split.
- Risk level 5 is rare, with 7 train examples and 2 dev examples.
- The label distributions are similar across the two splits.

### What this means
The dataset has an uneven label distribution. In particular, there are very few examples of risk level 5. This is worth keeping in mind when comparing models.

### Limitations
This analysis only looks at label counts and percentages. It does not explain why examples receive their labels or measure model performance for each risk level.

### Next steps
1. Keep the label distribution results for later analysis.
2. Evaluate future models using MAE and inspect errors across risk levels.
3. Continue with a simple text-based baseline after documenting this analysis.
