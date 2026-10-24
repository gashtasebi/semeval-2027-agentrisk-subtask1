import json
from collections import Counter, defaultdict
from pathlib import Path

TRAIN_PATH = Path("data/raw/train.jsonl")
DEV_PATH = Path("data/raw/dev.jsonl")
MANIFEST_PATH = Path("data/metadata/split_manifest.jsonl")


def read_jsonl(path):
    if not path.is_file():
        raise FileNotFoundError(f"File not found: {path}")

    records = []
    with path.open(encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            if not line.strip():
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError as error:
                raise ValueError(
                    f"Invalid JSON in {path}, line {line_number}: {error}"
                ) from error
    return records


def unique_ids(records, name):
    ids = [record.get("example_id") for record in records]

    if any(not isinstance(example_id, str) or not example_id
           for example_id in ids):
        raise ValueError(f"{name} contains a missing or invalid example_id")

    duplicates = len(ids) - len(set(ids))
    if duplicates:
        raise ValueError(f"{name} contains {duplicates} duplicate IDs")

    return set(ids)


def main():
    train = read_jsonl(TRAIN_PATH)
    dev = read_jsonl(DEV_PATH)
    manifest = read_jsonl(MANIFEST_PATH)

    required = {"example_id", "split", "scenario_group"}
    for index, record in enumerate(manifest, start=1):
        missing = required - record.keys()
        if missing:
            raise ValueError(
                f"Manifest record {index} is missing fields: {sorted(missing)}"
            )

    train_ids = unique_ids(train, "Train")
    dev_ids = unique_ids(dev, "Dev")
    manifest_ids = unique_ids(manifest, "Manifest")

    if train_ids & dev_ids:
        raise ValueError("Example IDs overlap between train and dev")

    manifest_by_id = {
        record["example_id"]: record for record in manifest
    }

    for split, ids in (("train", train_ids), ("dev", dev_ids)):
        missing = ids - manifest_ids
        if missing:
            raise ValueError(
                f"{len(missing)} {split} IDs are missing from manifest"
            )

        mismatches = {
            example_id for example_id in ids
            if manifest_by_id[example_id]["split"] != split
        }
        if mismatches:
            raise ValueError(
                f"{len(mismatches)} {split} IDs have incorrect manifest splits"
            )

    data_ids = train_ids | dev_ids
    extra_ids = manifest_ids - data_ids
    if extra_ids:
        raise ValueError(
            f"{len(extra_ids)} manifest IDs are absent from train/dev"
        )

    unexpected_splits = {
        record["split"] for record in manifest
    } - {"train", "dev"}
    if unexpected_splits:
        raise ValueError(f"Unexpected split values: {sorted(unexpected_splits)}")

    groups_by_split = defaultdict(set)
    for record in manifest:
        groups_by_split[record["split"]].add(record["scenario_group"])

    shared_groups = (
        groups_by_split["train"] & groups_by_split["dev"]
    )
    if shared_groups:
        raise ValueError(
            f"{len(shared_groups)} scenario groups overlap between train and dev"
        )

    print("Split validation passed.")
    print(f"Train records: {len(train_ids)}")
    print(f"Dev records: {len(dev_ids)}")
    print(f"Manifest records: {len(manifest_ids)}")
    print(f"Train scenario groups: {len(groups_by_split['train'])}")
    print(f"Dev scenario groups: {len(groups_by_split['dev'])}")
    print(f"Shared scenario groups: {len(shared_groups)}")


if __name__ == "__main__":
    main()
