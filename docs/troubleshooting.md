# Troubleshooting Notes

## SSH connection refused

1. Confirm the Ubuntu VM is running.
2. Check its current IP address.
3. Verify the SSH service with `sudo systemctl status ssh`.
4. Confirm the client is using the correct username and address.
5. Review the selected VirtualBox network mode.

## Wazuh agent does not enroll

1. Confirm the manager address from the endpoint.
2. Confirm the manager and endpoint clocks are correct.
3. Check the Wazuh manager log at `/var/ossec/logs/ossec.log`.
4. Check the Windows agent log.
5. Confirm required ports and VirtualBox network connectivity.

## Sysmon events do not appear

1. Open Event Viewer and confirm events exist under `Microsoft-Windows-Sysmon/Operational`.
2. Confirm the Wazuh agent configuration contains the correct event-channel location.
3. Restart the Wazuh agent after validating its configuration.
4. Search Wazuh using a known timestamp and endpoint name.

## Custom rule does not match

1. Examine the decoded event to confirm its field names.
2. Test the event with `wazuh-logtest`.
3. Confirm the custom rule ID is unique and within the custom range.
4. Confirm the parent rule or group matches the installed Wazuh ruleset.
5. Check the Wazuh manager log before restarting services.
