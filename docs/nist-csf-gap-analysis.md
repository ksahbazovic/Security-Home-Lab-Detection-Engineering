# Control Assessment — NIST CSF Gap Analysis

## Executive summary

This assessment reviews the Security Home Lab against the six functions of the NIST Cybersecurity Framework 2.0: Govern, Identify, Protect, Detect, Respond, and Recover. The assessment covers the planned three-system environment: a Windows endpoint, Linux server, and Wazuh SIEM.

The design, Linux foundation, documentation, detection content, and Python analysis tool are established. The largest current gaps are centralized monitoring deployment, endpoint enrollment, live detection validation, response testing, and recovery testing. These gaps are expected because the project remains in progress.

## Scope

- VirtualBox host and virtual-machine design
- Ubuntu Server endpoint and SSH administration
- Windows endpoint with Sysmon
- Wazuh server, indexer, dashboard, and agents
- Custom detection rules and MITRE ATT&CK mappings
- Python Sysmon-log parser
- Alert investigation and recovery procedures

## Rating method

| Risk | Definition |
|---|---|
| High | The gap significantly limits security visibility, access control, detection, or recovery |
| Medium | The gap reduces assurance or operational reliability |
| Low | The gap mainly affects documentation, maintenance, or efficiency |

| Status | Definition |
|---|---|
| Implemented | Completed and supported by available evidence |
| Partially implemented | Some required elements are complete |
| Planned | Designed or documented but awaiting deployment |
| Not implemented | No control or procedure is currently present |

## Findings summary

| ID | NIST CSF function | Finding | Risk | Status |
|---|---|---|---|---|
| F-01 | Identify | Asset inventory lacks final versions, addresses, and ownership data | Low | Partially implemented |
| F-02 | Protect | SSH hardening has not been fully reviewed | Medium | Partially implemented |
| F-03 | Detect | Central Wazuh event collection is not yet validated | High | Planned |
| F-04 | Detect | Custom detection rules require live-event testing and tuning | High | Partially implemented |
| F-05 | Respond | Alert-triage procedure has not been exercised | Medium | Partially implemented |
| F-06 | Recover | VM snapshot and recovery process has not been tested | Medium | Planned |

## Detailed findings

### F-01: Incomplete asset inventory

- **Function:** Identify
- **Condition:** The architecture identifies the Windows endpoint, Linux server, Wazuh SIEM, and macOS host. Final software versions, IP addressing, and deployment dates have not been recorded.
- **Risk:** Low
- **Impact:** Troubleshooting, change tracking, and reproducibility may be slower.
- **Recommendation:** Record the operating system, allocated resources, software versions, network role, and deployment date for each system.
- **Priority:** 5
- **Evidence:** `docs/architecture.md`, `docs/setup-notes.md`

### F-02: SSH configuration requires hardening review

- **Function:** Protect
- **Condition:** SSH remote administration works on the Ubuntu Server. Authentication settings, root-login policy, firewall rules, and failed-login handling have not yet been documented as reviewed.
- **Risk:** Medium
- **Impact:** Weak remote-administration settings could increase the risk of unauthorized access inside the lab environment.
- **Recommendation:** Review `sshd_config`, disable direct root login, document the selected authentication method, enable the host firewall, and record the resulting configuration.
- **Priority:** 3
- **Evidence:** Successful SSH administration; final configuration evidence pending

### F-03: Centralized monitoring is not yet validated

- **Function:** Detect
- **Condition:** Wazuh installation and endpoint enrollment procedures are planned, but end-to-end event delivery has not yet been demonstrated.
- **Risk:** High
- **Impact:** Endpoint activity cannot be centrally searched, correlated, or alerted on until collection is working.
- **Recommendation:** Install the Wazuh central components, enroll both endpoints, verify their active status, and capture a known event from each system.
- **Priority:** 1
- **Evidence:** `configs/wazuh-agent-sysmon.xml`, `docs/test-plan.md`; live dashboard evidence pending

### F-04: Detection rules require validation and tuning

- **Function:** Detect
- **Condition:** Three custom rules have been written and mapped to MITRE ATT&CK, but their parent groups, field names, expected matches, and false-positive behavior require testing with live decoded events.
- **Risk:** High
- **Impact:** Untested logic may fail to alert or may generate unnecessary alerts.
- **Recommendation:** Test every rule with `wazuh-logtest`, generate one controlled matching event and one benign nonmatching event, then document tuning decisions.
- **Priority:** 2
- **Evidence:** `detections/local_rules.xml`, `docs/detection-catalog.md`

### F-05: Response process has not been exercised

- **Function:** Respond
- **Condition:** An alert-triage workflow exists, but no completed alert record demonstrates that it has been followed.
- **Risk:** Medium
- **Impact:** Investigation steps may be inconsistent when an alert occurs.
- **Recommendation:** Use the first validated custom alert to perform a complete triage exercise and record the classification, evidence, actions, and rule-tuning decision.
- **Priority:** 4
- **Evidence:** `docs/incident-response-playbook.md`; completed alert record pending

### F-06: Recovery procedure is untested

- **Function:** Recover
- **Condition:** The project does not yet contain evidence that a VM snapshot, configuration backup, or restore operation has been tested.
- **Risk:** Medium
- **Impact:** A configuration mistake or failed update could require rebuilding a system and delay the project.
- **Recommendation:** Create a documented snapshot or backup, make a harmless test change, restore the system, and confirm normal operation.
- **Priority:** 6
- **Evidence:** Recovery evidence pending

## Prioritized remediation plan

1. Deploy Wazuh and validate event ingestion.
2. Test and tune the three custom rules.
3. Review and document SSH hardening.
4. Complete one alert-triage exercise.
5. Complete the asset inventory.
6. Test VM snapshot recovery.

## Evidence register

| Evidence ID | Description | Status |
|---|---|---|
| E-01 | Ubuntu Server VirtualBox configuration | Pending sanitized screenshot |
| E-02 | Successful SSH administration | Completed; sanitized screenshot pending |
| E-03 | Wazuh dashboard access | Pending deployment |
| E-04 | Windows agent enrolled and active | Pending deployment |
| E-05 | Sysmon Event ID 1 received by Wazuh | Pending validation |
| E-06 | Three custom rules tested successfully | Pending validation |
| E-07 | Python parser test results | Completed |
| E-08 | Completed alert-triage record | Pending exercise |
| E-09 | Successful VM recovery test | Pending exercise |

## Conclusion

The lab currently demonstrates virtualization, Linux server administration, repository documentation, detection-rule development, MITRE ATT&CK mapping, and Python log processing. Central monitoring, live detection output, response execution, and recovery testing remain the main implementation priorities. The assessment will be updated with screenshots, event records, and validation results as those tasks are completed.
