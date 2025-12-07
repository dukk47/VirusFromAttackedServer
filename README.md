# Virus Samples from Attacked Server

Collected on: 2025-12-07

## Files

### linux.sh
Malicious script downloaded every minute via cronjob from `https://repositorylinux.xyz/linux.sh`
- Downloads and executes `linuxsys` cryptominer
- Sources: GitHub (whereveryouare666/linuxsys), pastebin, dodoma.shop

### fake-curl
Trojanized curl binary placed in `/usr/local/bin/curl` to intercept curl commands
- Statically linked, stripped ELF binary
- Likely used to inject mining payloads

## Persistence Mechanisms Found

1. **Crontab entries** - Running every minute to reinfect
2. **Systemd services** - `dspool_miner.service`, `system-daemon.service`
3. **profile.d script** - `/etc/profile.d/.kworker.sh` backdoor
4. **Trojanized binaries** - Fake curl in /usr/local/bin/

## C2 Infrastructure

- `repositorylinux.xyz` - Main payload server
- `80.64.16.241` - Secondary C2
- `pool.hashvault.pro` - Mining pool (Monero)
- `auto.c3pool.org` - Mining pool
