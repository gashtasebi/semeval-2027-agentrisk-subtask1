import json
from pathlib import Path
from statistics import mean


PROJECT_ROOT = Path(__file__).resolve().parents[2]
TRAIN_PATH = PROJECT_ROOT / "data" / "raw" / "train.jsonl"
DEV_PATH = PROJECT_ROOT / "data" / "raw" / "dev.jsonl"


def load_jsonl(path):
    with path.open("r", encoding="utf-8") as file:
        return [json.loads(line) for line in file if line.strip()]


def calculate_mae(predictions, gold_labels):
    if len(predictions) != len(gold_labels):
        raise ValueError("Predictions and gold labels must have equal lengths.")
    if not gold_labels:
        raise ValueError("Cannot calculate MAE for an empty dataset.")

    return sum(
        abs(pred - gold)
        for pred, gold in zip(predictions, gold_labels)
    ) / len(gold_labels)


def main():
    train = load_jsonl(TRAIN_PATH)
    dev = load_jsonl(DEV_PATH)

    train_labels = [int(row["risk_severity"]) for row in train]
    dev_labels = [int(row["risk_severity"]) for row in dev]

    if not train_labels:
        raise ValueError("Training dataset is empty.")

    prediction = mean(train_labels)
    predictions = [prediction] * len(dev_labels)
    mae = calculate_mae(predictions, dev_labels)

    print("Baseline: constant mean prediction")
    print(f"Train examples: {len(train_labels)}")
    print(f"Dev examples: {len(dev_labels)}")
    print(f"Train label mean: {prediction:.6f}")
    print(f"Dev MAE: {mae:.6f}")


if __name__ == "__main__":
    main()
