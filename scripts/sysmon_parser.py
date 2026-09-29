#!/usr/bin/env python3
"""Normalize Sysmon-style JSON or Wazuh alert JSON into JSON or CSV.

The parser uses only the Python standard library and accepts one JSON object per
line. It supports both a direct event structure and the nested `data.win`
structure commonly present in exported Wazuh alerts.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any, Iterable

FIELDS = [
    "event_id", "utc_time", "computer", "user", "image", "command_line",
    "parent_image", "parent_command_line", "process_id", "process_guid", "hashes",
]


def deep_get(record: dict[str, Any], path: str) -> Any:
    value: Any = record
    for part in path.split("."):
        if not isinstance(value, dict) or part not in value:
            return None
        value = value[part]
    return value


def first_value(record: dict[str, Any], *paths: str, default: str = "") -> str:
    for path in paths:
        value = deep_get(record, path)
        if value is not None and value != "":
            return str(value)
    return default


def normalize_event(record: dict[str, Any]) -> dict[str, str]:
    """Return a stable set of fields from a Sysmon or Wazuh JSON record."""
    return {
        "event_id": first_value(record, "data.win.system.eventID", "win.system.eventID", "EventID", "event_id"),
        "utc_time": first_value(record, "data.win.eventdata.utcTime", "win.eventdata.utcTime", "UtcTime", "utc_time", "timestamp"),
        "computer": first_value(record, "data.win.system.computer", "win.system.computer", "Computer", "computer"),
        "user": first_value(record, "data.win.eventdata.user", "win.eventdata.user", "User", "user"),
        "image": first_value(record, "data.win.eventdata.image", "win.eventdata.image", "Image", "image"),
        "command_line": first_value(record, "data.win.eventdata.commandLine", "win.eventdata.commandLine", "CommandLine", "command_line"),
        "parent_image": first_value(record, "data.win.eventdata.parentImage", "win.eventdata.parentImage", "ParentImage", "parent_image"),
        "parent_command_line": first_value(record, "data.win.eventdata.parentCommandLine", "win.eventdata.parentCommandLine", "ParentCommandLine", "parent_command_line"),
        "process_id": first_value(record, "data.win.eventdata.processId", "win.eventdata.processId", "ProcessId", "process_id"),
        "process_guid": first_value(record, "data.win.eventdata.processGuid", "win.eventdata.processGuid", "ProcessGuid", "process_guid"),
        "hashes": first_value(record, "data.win.eventdata.hashes", "win.eventdata.hashes", "Hashes", "hashes"),
    }


def load_jsonl(path: Path) -> Iterable[dict[str, Any]]:
    with path.open(encoding="utf-8") as source:
        for line_number, line in enumerate(source, start=1):
            if not line.strip():
                continue
            try:
                value = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON on line {line_number}: {exc.msg}") from exc
            if not isinstance(value, dict):
                raise ValueError(f"Line {line_number} must contain a JSON object")
            yield value


def write_json(records: list[dict[str, str]], destination: Path | None) -> None:
    output = json.dumps(records, indent=2)
    if destination:
        destination.write_text(output + "\n", encoding="utf-8")
    else:
        print(output)


def write_csv(records: list[dict[str, str]], destination: Path | None) -> None:
    if destination:
        with destination.open("w", newline="", encoding="utf-8") as target:
            writer = csv.DictWriter(target, fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(records)
    else:
        import sys
        writer = csv.DictWriter(sys.stdout, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(records)


def main() -> None:
    parser = argparse.ArgumentParser(description="Normalize Sysmon or Wazuh JSONL events")
    parser.add_argument("input", type=Path, help="Input JSONL file")
    parser.add_argument("--format", choices=("json", "csv"), default="json")
    parser.add_argument("--output", type=Path, help="Optional output path")
    args = parser.parse_args()

    records = [normalize_event(record) for record in load_jsonl(args.input)]
    if args.format == "csv":
        write_csv(records, args.output)
    else:
        write_json(records, args.output)


if __name__ == "__main__":
    main()
