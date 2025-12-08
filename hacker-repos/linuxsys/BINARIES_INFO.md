# Binaries from whereveryouare666/linuxsys

**WARNING:** These binaries are malware and should NOT be downloaded to your system.

## Files in Repository

| File | Size | SHA (from GitHub) | Purpose |
|------|------|-------------------|---------|
| linux.bin | 6.7 MB | [Check GitHub API] | XMRig Monero Miner (Linux) |
| winsys.exe | 7.9 MB | [Check GitHub API] | XMRig Monero Miner (Windows) |
| nssm.exe | 288 KB | [Check GitHub API] | Non-Sucking Service Manager (Persistence) |
| config.json | 1.3 KB | [Downloaded] | XMRig Mining Configuration |

## Download URLs (for reference only)

```
https://raw.githubusercontent.com/whereveryouare666/linuxsys/main/linux.bin
https://raw.githubusercontent.com/whereveryouare666/linuxsys/main/winsys.exe
https://raw.githubusercontent.com/whereveryouare666/linuxsys/main/nssm.exe
https://raw.githubusercontent.com/whereveryouare666/linuxsys/main/config.json
```

## Analysis

### linux.bin
- XMRig-based Monero miner compiled for Linux x64
- Connects to `cyberknull.publicvm.com:80`
- Uses Stratum protocol on HTTP port for firewall bypass

### winsys.exe
- XMRig-based Monero miner compiled for Windows
- Same configuration as Linux version
- Likely uses nssm.exe for service persistence

### nssm.exe
- "Non-Sucking Service Manager" - legitimate tool
- Used by attacker to install winsys.exe as Windows service
- Provides persistence across reboots

## config.json Summary

```json
{
  "pools": [{
    "url": "cyberknull.publicvm.com:80",
    "pass": "lucifer",
    "tls": false
  }],
  "cpu": {
    "max-threads-hint": 100
  },
  "background": true,
  "watch": true,
  "donate-level": 0
}
```

---

*Binaries not downloaded for safety - only metadata documented*
