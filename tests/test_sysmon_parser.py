import json
import tempfile
import unittest
from pathlib import Path

from scripts.sysmon_parser import load_jsonl, normalize_event


class SysmonParserTests(unittest.TestCase):
    def test_normalizes_wazuh_event(self):
        event = {
            "data": {
                "win": {
                    "system": {"eventID": "1", "computer": "WIN-LAB"},
                    "eventdata": {
                        "utcTime": "2026-09-29 20:00:00.000",
                        "user": "LAB\\student",
                        "image": "C:\\Windows\\System32\\whoami.exe",
                        "commandLine": "whoami.exe /all",
                        "parentImage": "C:\\Windows\\System32\\cmd.exe",
                        "processId": "4242",
                    },
                }
            }
        }
        result = normalize_event(event)
        self.assertEqual("1", result["event_id"])
        self.assertEqual("WIN-LAB", result["computer"])
        self.assertTrue(result["image"].endswith("whoami.exe"))
        self.assertEqual("whoami.exe /all", result["command_line"])

    def test_normalizes_flat_event(self):
        event = {"EventID": 1, "Image": "powershell.exe", "CommandLine": "Write-Output lab-test"}
        result = normalize_event(event)
        self.assertEqual("1", result["event_id"])
        self.assertEqual("powershell.exe", result["image"])
        self.assertEqual("", result["computer"])

    def test_rejects_invalid_jsonl(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.jsonl"
            path.write_text('{"valid": true}\nnot-json\n', encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "line 2"):
                list(load_jsonl(path))


if __name__ == "__main__":
    unittest.main()
