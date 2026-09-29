# Lab Alert-Triage Playbook

## Purpose

This short playbook defines how alerts generated in the lab will be reviewed and documented.

## Workflow

1. **Identify:** Record the Wazuh rule ID, alert level, endpoint, event time, and MITRE mapping.
2. **Validate:** Compare the alert to the planned lab test and review the full process command line and parent process.
3. **Scope:** Search for related events using the process GUID, user, image, and surrounding timestamps.
4. **Classify:** Mark the event as expected test activity, benign activity, false positive, or unexplained activity.
5. **Contain:** If the event is unexpected, pause the affected VM and disconnect its virtual network while preserving logs.
6. **Document:** Save sanitized evidence and record the decision in the test results.
7. **Improve:** Tune the rule or update the procedure based on the evidence.

## Alert record template

- Alert ID:
- Date and time:
- Endpoint:
- Rule and level:
- MITRE technique:
- Process and command line:
- Parent process:
- Classification:
- Evidence reviewed:
- Action taken:
- Rule-tuning decision:
