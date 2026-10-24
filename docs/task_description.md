# AgentRisk — Subtask 1: Risk Level Estimation

## 1. Project Scope

This research project focuses exclusively on Subtask 1 (Risk Level Estimation)
of AgentRisk, SemEval 2027 Task 10.

The task asks how risky it is to execute the final proposed action in the
context of the preceding multi-turn agent interaction.

Other AgentRisk subtasks are outside the scope of this project.

## 2. Sources

- Dataset repository:
  https://huggingface.co/datasets/AgentRisk/agentrisk-data-2027
- Dataset README:
  https://huggingface.co/datasets/AgentRisk/agentrisk-data-2027/blob/main/README.md
- Shared task page:
  https://agentrisk-semeval.lovable.app/
- Dataset date accessed: 2026-10-24

The dataset details in this document are based on the README content inspected
on the access date above. The official evaluation instructions and submission
format still need to be checked separately.

## 3. Task Definition

Given a multi-turn agent interaction and its final proposed action, estimate
the risk severity of executing that action.

The proposed action must be assessed in the context of the preceding
interaction, rather than in isolation.

## 4. Input and Target Fields

According to the dataset README:

| Field | Type | Role |
|---|---|---|
| `example_id` | string | Unique example identifier |
| `formatted_interaction` | string | Interaction trajectory; the final step is the proposed action |
| `proposed_action` | string | Final proposed action, identical to the last step |
| `risk_severity` | integer | Subtask 1 target label, from 1 to 5 |
| `risk_domains` | list of strings | Subtask 2a labels; outside this project's prediction scope |
| `risk_drivers` | list of strings | Subtask 2b labels; outside this project's prediction scope |

For Subtask 1, the target variable is `risk_severity`.

The relationship between `formatted_interaction` and `proposed_action` should
be considered during later data inspection and baseline design. Since the
README states that the final step in `formatted_interaction` is identical to
`proposed_action`, experiments should document which input representation
they use.

## 5. Risk Severity Labels

The dataset README defines the following ordinal severity levels:

| Label | Name |
|---:|---|
| 1 | Minimal |
| 2 | Low |
| 3 | Moderate |
| 4 | High |
| 5 | Critical |

Severity is assessed within the relevant consequence domain.

## 6. Dataset Splits

The dataset README reports the following sizes:

| Split | Number of examples |
|---|---:|
| `train` | 568 |
| `dev` | 143 |
| Total | 711 |

The repository lists these data files:

- `data/train.jsonl`
- `data/dev.jsonl`

The README also describes `metadata/split_manifest.jsonl`, which maps each
`example_id` to its split and scenario group.

Items derived from the same scenario are kept in the same split to reduce
scenario leakage between training and development data. The README states
that the split is stratified so labels occur in both splits in similar
proportions.

These counts and split properties must be rechecked during local data
inspection before experiments are run.

## 7. Evaluation

The primary metric for Subtask 1 is Mean Absolute Error (MAE).

For true labels y_i and predictions y_hat_i:

MAE = (1 / N) * sum_i |y_i - y_hat_i|

Lower MAE indicates better predictions.

The dataset README states that supplementary metrics, ranking details, and
submission instructions will be announced ahead of the evaluation period.
The official evaluation instructions therefore remain to be verified.

## 8. Scope Exclusions

This project does not currently address:

- Subtask 2a: Harm Domain Classification
- Subtask 2b: Risk Driver Classification
- Subtask 3: Policy-Guided Intervention

The fields `risk_domains` and `risk_drivers` may be inspected to understand
the dataset, but they are not prediction targets for this project.

## 9. Current Research Status

As of 2026-10-24:

- The dataset repository and README have been located and inspected.
- The dataset has not yet been downloaded or inspected locally.
- No experiments have been run.
- No model performance results are available.
- The official evaluation and submission instructions have not yet been
  independently verified.

## 10. Next Steps

1. Inspect the repository's available files and dataset loading instructions.
2. Download the relevant data locally without committing raw data to Git.
3. Verify the schema, label values, missing values, duplicates, and split sizes.
4. Inspect risk severity distribution in the training and development splits.
5. Review the official evaluation instructions.
6. Establish a simple, reproducible baseline before trying more complex models.
7. Record each experiment, configuration, result, and code commit.
