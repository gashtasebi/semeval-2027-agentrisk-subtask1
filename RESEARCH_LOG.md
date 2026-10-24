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
