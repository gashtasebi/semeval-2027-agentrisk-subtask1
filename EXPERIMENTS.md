
## Experiment 001 — Constant Median Baseline

**Date:** 2026-10-24
**Subtask:** 1 — Risk Level Estimation
**Status:** Completed

### Objective
Establish a simple reference score before testing more complex models.

### Method
- Training data: official train split (568 examples).
- Evaluation data: official dev split (143 examples).
- Prediction: the median `risk_severity` in the training split, used as a constant prediction for every dev example.
- Metric: Mean Absolute Error (MAE).
- Implementation: `src/agentrisk/baseline_median.py`.
- Dependencies: Python standard library only.

### Results
- Training examples: 568
- Dev examples: 143
- Training-label median: 2
- Dev MAE: 1.216783

### Interpretation
This result provides a simple reference point for subsequent experiments. It does not establish whether a more complex model will perform better.

### Limitations
- This baseline does not use interaction text or proposed actions.
- It predicts the same risk level for every dev example.
- The result is based on one fixed official train/dev split.
- No uncertainty estimate or repeated evaluation has been computed.

### Next Steps
1. Add automated tests for the baseline and MAE calculation.
2. Compare future models against this reference using the same dev split.
3. Record all model choices and results before drawing conclusions.

## Experiment 002 — Constant Mean Baseline

**Date:** 2026-10-24
**Subtask:** 1 — Risk Level Estimation
**Status:** Completed

### Objective
Compare a constant mean prediction with the median baseline.

### Method
- Training data: official train split (568 examples).
- Evaluation data: official dev split (143 examples).
- Prediction: the mean `risk_severity` in the training split, used for every dev example.
- Metric: Mean Absolute Error (MAE).
- Implementation: `src/agentrisk/baseline_mean.py`.
- Dependencies: Python standard library only.

### Results
- Training examples: 568
- Dev examples: 143
- Mean training label: 2.272887
- Dev MAE: 1.226325

### Interpretation
The mean baseline had a slightly higher MAE than the median baseline (1.216783). On this dev split, the median baseline performed better.

### Limitations
This baseline does not use the interaction text or proposed action. It makes the same prediction for every dev example.

### Next Steps
1. Run the automated tests and check the code changes.
2. Keep both baseline results for comparison with future models.
3. Start exploring methods that use the interaction text.
