import json
from collections import Counter
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
TRAIN_PATH = PROJECT_ROOT / "data" / "raw" / "train.jsonl"
DEV_PATH = PROJECT_ROOT / "data" / "raw" / "dev.jsonl"


def load_labels(path):
    with path.open("r", encoding="utf-8") as file:
        return [
            int(json.loads(line)["risk_severity"])
            for line in file
            if line.strip()
        ]


def print_distribution(name, labels):
    counts = Counter(labels)
    total = len(labels)

    print(f"\n{name} label distribution")
    print(f"Total examples: {total}")
    print("Label | Count | Percentage")

    for label in range(1, 6):
        count = counts[label]
        percentage = count / total * 100 if total else 0
        print(f"{label:5} | {count:5} | {percentage:9.2f}%")


def main():
    train_labels = load_labels(TRAIN_PATH)
    dev_labels = load_labels(DEV_PATH)

    print_distribution("Train", train_labels)
    print_distribution("Dev", dev_labels)


if __name__ == "__main__":
    main()
