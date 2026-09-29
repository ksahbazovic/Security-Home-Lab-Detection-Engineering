# Detection Test Plan

> **Status:** Procedures drafted; execution evidence pending

All tests are performed only inside the isolated lab on systems owned and administered by the project author.

## Test 1: Basic process telemetry

**Purpose:** Confirm that Sysmon Event ID 1 reaches Wazuh.

**Procedure:**

1. Start the Wazuh server and Windows endpoint.
2. Confirm that the Wazuh agent is connected.
3. Open Command Prompt on the Windows lab endpoint.
4. Run `whoami /all`.
5. Search Wazuh for a process creation event containing `whoami.exe`.
6. Record the timestamp, agent, event ID, and sanitized screenshot.

**Expected result:** Wazuh displays a Sysmon process-creation event containing the image, command line, user, and parent process.

**Observed result:** Pending.

## Test 2: PowerShell process creation

**Purpose:** Confirm command-line visibility for PowerShell.

**Procedure:**

1. Open PowerShell on the Windows lab endpoint.
2. Run `Write-Output "lab-test"`.
3. Search Wazuh for the corresponding Sysmon Event ID 1 record.
4. Verify the image, command line, parent image, and user fields.

**Expected result:** The event is collected and searchable. The encoded-command rule should not trigger because the safe command does not use encoded input.

**Observed result:** Pending.

## Test 3: Custom-rule validation

**Purpose:** Validate each draft rule without depending on uncontrolled activity.

**Procedure:**

1. Copy a sanitized event into the Wazuh rule-testing tool.
2. Run `wazuh-logtest` on the Wazuh server.
3. Confirm the matched rule ID, level, description, and MITRE mapping.
4. Revise field names or parent groups if the rule fails.
5. Restart the manager only after the configuration passes validation.

**Expected result:** Each sample matches only its intended rule.

**Observed result:** Pending.

## Evidence checklist

- [ ] Windows endpoint shown as active in Wazuh
- [ ] Sysmon Event ID 1 displayed in Wazuh
- [ ] Custom rule output from `wazuh-logtest`
- [ ] Custom alert visible in the dashboard
- [ ] False-positive or tuning note for each rule
