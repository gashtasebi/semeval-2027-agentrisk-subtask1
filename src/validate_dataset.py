import json
from collections import Counter
from pathlib import Path

REQUIRED_FIELDS = {
    "example_id",
    "formatted_interaction",
    "proposed_action",
    "risk_severity",
}


def validate_file(path: Path) -> None:
    records = []
    errors = []

    with path.open(encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            if not line.strip():
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError as error:
                errors.append(f"Line {line_number}: {error}")

    label_counts = Counter()
    missing_fields = Counter()
    invalid_labels = []
    example_ids = []

    for index, record in enumerate(records, start=1):
        if not isinstance(record, dict):
            errors.append(f"Record {index} is not a JSON object")
            continue

        missing_fields.update(REQUIRED_FIELDS - record.keys())

        label = record.get("risk_severity")
        if type(label) is int and 1 <= label <= 5:
            label_counts[label] += 1
        else:
            invalid_labels.append((index, label))

        if "example_id" in record:
            example_ids.append(record["example_id"])

    duplicate_ids = len(example_ids) - len(set(example_ids))

    print(f"\n--- {path} ---")
    print(f"Records parsed: {len(records)}")
    print(f"JSON errors: {len(errors)}")
    print(f"Risk severity counts: {dict(sorted(label_counts.items()))}")
    print(f"Missing required fields: {dict(missing_fields)}")
    print(f"Invalid risk labels: {len(invalid_labels)}")
    print(f"Duplicate IDs within file: {duplicate_ids}")

    if errors:
        print("First error:", errors[0])
    if invalid_labels:
        print("First invalid label:", invalid_labels[0])

    if errors or missing_fields or invalid_labels or duplicate_ids:
        raise SystemExit(f"Validation failed for {path}")


def main() -> None:
    for filename in ("data/raw/train.jsonl", "data/raw/dev.jsonl"):
        path = Path(filename)
        if not path.is_file():
            raise FileNotFoundError(f"Dataset file not found: {path}")
        validate_file(path)

    print("\nBasic dataset validation passed.")


if __name__ == "__main__":
    main()
