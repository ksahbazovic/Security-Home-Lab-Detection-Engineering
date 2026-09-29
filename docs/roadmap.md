# Project Roadmap

## Phase 1: Foundation

- [x] Install VirtualBox on the Apple Silicon host
- [x] Create the Ubuntu Server ARM64 VM
- [x] Enable SSH and connect from macOS Terminal
- [x] Update the Ubuntu Server
- [x] Create the GitHub repository and documentation structure

## Phase 2: Central monitoring

- [ ] Create or prepare the Wazuh server environment
- [ ] Install the Wazuh server, indexer, and dashboard
- [ ] Record the installed versions and resource allocation
- [ ] Open the dashboard from the macOS host
- [ ] Capture sanitized installation evidence

## Phase 3: Windows telemetry

- [ ] Create a Windows 11 ARM virtual machine
- [ ] Install Sysmon with a documented configuration
- [ ] Install and enroll the Wazuh agent
- [ ] Verify Windows events in the Wazuh dashboard
- [ ] Capture sanitized event evidence

## Phase 4: Detection engineering

- [ ] Define safe test cases
- [ ] Generate controlled events inside the lab
- [ ] Review the resulting Sysmon and Wazuh events
- [ ] Create custom Wazuh detection rules
- [ ] Map each rule to an appropriate MITRE ATT&CK technique
- [ ] Record false positives and tuning decisions

## Phase 5: Python analysis

- [x] Create a synthetic, sanitized Sysmon event sample for development
- [x] Write the initial Python parser
- [x] Normalize selected fields into JSON or CSV
- [x] Add command-line usage instructions
- [x] Test the parser against the synthetic sample

## Phase 6: Live-data parser validation

- [ ] Export a sanitized Sysmon event from the completed lab
- [ ] Confirm the parser handles the live Wazuh export format
- [ ] Adjust field mappings if required

## Phase 7: Assessment and presentation

- [ ] Complete the NIST CSF gap analysis using observed evidence
- [ ] Assign risk ratings and recommendations
- [ ] Add final screenshots and diagrams
- [ ] Review the repository for secrets and personal information
- [ ] Update the resume with the verified rule count and project link
