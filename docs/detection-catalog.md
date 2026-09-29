# Detection Catalog

> **Status:** Draft rules awaiting live Wazuh validation

| Rule ID | Detection | Data source | MITRE ATT&CK | Severity | Validation |
|---|---|---|---|---|---|
| 100100 | Encoded PowerShell arguments | Sysmon Event ID 1 | T1059.001 | 8 | Pending |
| 100101 | Certutil with download-related arguments | Sysmon Event ID 1 | T1105 | 7 | Pending |
| 100102 | Rundll32 execution | Sysmon Event ID 1 | T1218.011 | 7 | Pending |

## Tuning approach

Each rule will be tested with a matching event and a benign nonmatching event. Field names, parent groups, severity, and descriptions will be updated from observed Wazuh output. Any common legitimate activity will be recorded before exclusions are considered.
