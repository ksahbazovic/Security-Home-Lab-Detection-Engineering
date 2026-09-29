# Python Sysmon Parser

`sysmon_parser.py` normalizes Sysmon-style JSONL and nested Wazuh alert JSONL into a stable set of fields. It uses only the Python standard library.

## Run

```bash
python3 scripts/sysmon_parser.py samples/sysmon_events.jsonl
python3 scripts/sysmon_parser.py samples/sysmon_events.jsonl --format csv --output normalized.csv
```

## Test

```bash
python3 -m unittest discover -s tests -v
```
