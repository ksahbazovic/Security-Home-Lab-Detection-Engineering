# Setup Notes

## Host system

- Apple Silicon Mac
- 16 GB memory
- Oracle VirtualBox
- Wi-Fi network connection

## Completed: Ubuntu Server VM

The first lab system is an Ubuntu Server ARM64 virtual machine named `Linux_Server`.

### Virtual hardware

- Memory: 2 GB
- Processors: 2 virtual CPUs
- Storage: 30 GB virtual disk
- Firmware: EFI enabled
- Network: VirtualBox NAT during the initial setup

### Configuration completed

1. Installed Ubuntu Server from an ARM64 image.
2. Created the local Linux user during installation.
3. Installed and enabled OpenSSH.
4. Confirmed that the server received an IP address.
5. Connected from macOS Terminal using SSH.
6. Updated installed packages from the remote terminal session.
7. Shut down the server cleanly through SSH.

### Validation performed

A successful SSH login confirmed that the host could reach and remotely administer the Linux VM. Package-management commands executed through that session confirmed basic system and network functionality.

## Evidence to add

The following evidence will be captured during the next lab session:

- Sanitized screenshot of the VirtualBox VM settings
- Sanitized SSH login screenshot
- Output showing the operating-system version
- Output showing the SSH service status

Sensitive values such as usernames, IP addresses, passwords, and host keys should be hidden before screenshots are published.

## Next setup tasks

- Allocate resources for the Wazuh server
- Install the Wazuh server, indexer, and dashboard
- Verify dashboard access from the Mac
- Create the Windows 11 ARM endpoint
- Install Sysmon and the Wazuh agent on Windows
- Confirm that Windows events reach Wazuh
