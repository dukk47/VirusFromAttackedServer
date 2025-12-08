# Virus Samples from Attacked Server

**Collected on:** 2025-12-07
**Analysis completed:** 2025-12-08
**Status:** Server cleaned, documentation complete

---

## Quick Links

| Dokument | Beschreibung |
|----------|--------------|
| [ANALYSIS.md](ANALYSIS.md) | Komplette forensische Analyse |
| [C2_INFRASTRUCTURE.md](C2_INFRASTRUCTURE.md) | Command & Control Infrastruktur |
| [attacker-profile/ATTACKER_PROFILE.md](attacker-profile/ATTACKER_PROFILE.md) | Profil des Angreifers |

---

## Infection Summary

This server was heavily compromised with **multiple persistence mechanisms** that reinstall each other.

### Attacker Information

| Attribut | Wert |
|----------|------|
| **GitHub User** | [whereveryouare666](https://github.com/whereveryouare666) |
| **User ID** | 119106426 |
| **Account erstellt** | 26. November 2022 |
| **Mining Proxy** | cyberknull.publicvm.com:80 |
| **Pool Passwort** | lucifer |

---

## Repository Structure

```
attack/
├── README.md                      # Diese Datei
├── ANALYSIS.md                    # Forensische Analyse
├── C2_INFRASTRUCTURE.md           # C2-Dokumentation
│
├── linux_malware.sh.txt           # Dropper-Skript (als .txt)
│
├── c2-config/
│   └── config.json                # XMRig Mining-Konfiguration
│
├── attacker-profile/
│   ├── ATTACKER_PROFILE.md        # Angreifer-Profil
│   └── webshells_list.txt         # Liste der Webshells
│
└── services/                      # Malicious systemd services
    ├── alive.service
    ├── lived.service
    ├── c3pool_miner.service
    ├── system-update-service.service
    ├── rsyslo.service
    ├── networkerd.service
    └── systemd-utils.service
```

---

## Binaries (vom Server gesammelt)

| File | Size | Location | Purpose |
|------|------|----------|---------|
| sshd-agent | 14MB | /usr/bin/sshd-agent | Main persistence trojan, restores cronjobs |
| systemd-daemon | 345KB | /bin/systemd-daemon | Secondary persistence |
| fake-curl | 3.4MB | /usr/local/bin/curl | Trojanized curl |
| rsyslo-binary | 1.4MB | /usr/local/rsyslo/rsyslo | Fake antivirus agent |

## Binaries (vom Angreifer-Repo)

| File | Size | Source | Purpose |
|------|------|--------|---------|
| linux.bin | 6.7 MB | github.com/whereveryouare666/linuxsys | XMRig Miner (Linux) |
| winsys.exe | 7.9 MB | github.com/whereveryouare666/linuxsys | XMRig Miner (Windows) |
| nssm.exe | 288 KB | github.com/whereveryouare666/linuxsys | Windows Service Manager |

---

## Malicious Services (in /etc/systemd/system/)

| Service | Binary | Purpose |
|---------|--------|---------|
| sshd-agent.service | /usr/bin/sshd-agent | Persistence |
| systemd-agent.service | /bin/systemd-daemon | Persistence |
| alive.service | /tmp/runenv/alive.sh | Watchdog |
| lived.service | /tmp/runenv/lived.sh | Watchdog |
| networkerd.service | /tmp/runvv/runvv | Unknown |
| c3pool_miner.service | xmrig | Monero miner |
| system-update-service.service | xmrig | Monero miner (hashvault) |
| rsyslo.service | /usr/local/rsyslo/rsyslo | Fake AV |
| systemd-utils.service | ntpclient | Fake NTP client (C2?) |

---

## Cronjob Persistence

Every minute downloads and executes:
- `https://repositorylinux.xyz/linux.sh` ✅ Captured in linux_malware.sh.txt
- `http://80.64.16.241/unk.sh` ❌ Offline

---

## C2 Infrastructure

### Primary C2 (Config-based):
| Server | URL | Status |
|--------|-----|--------|
| GitHub | github.com/whereveryouare666/linuxsys | ✅ Active |
| Pastebin | pastebin.com/raw/5LRZX6XQ | ✅ Active |
| WordPress | dodoma.shop | ⚠️ Unknown |

### Secondary C2 (Dropper):
| Server | URL | Status |
|--------|-----|--------|
| repositorylinux.xyz | https://repositorylinux.xyz/linux.sh | ✅ Active |
| 80.64.16.241 | http://80.64.16.241/unk.sh | ❌ Offline |

### Mining Infrastructure:
| Server | Purpose |
|--------|---------|
| cyberknull.publicvm.com:80 | Eigener Stratum Proxy |
| pool.hashvault.pro:443 | Public Mining Pool |
| auto.c3pool.org | Public Mining Pool |

---

## Monero Wallets

```
# Hashvault Pool
88tGYBwhWNzGesQs5QkwE1PdBa1tXGb9dcjxrdwujU3SEs3i7psaoJc4KmrDvv4VPTNtXazDWGkvGGfqurdBggvPEhZ43DJ

# C3Pool
46d2vayVr8k8yH6YKLBsDsY8PNo2oqK7xeCiuECsLAsiTBiqNt6nkMPHQfi1vHTRzmAQyS9spDsnHcBnoeyxgVD1HLNNsLB
```

---

## IOCs (Indicators of Compromise)

### Domains:
```
repositorylinux.xyz
cyberknull.publicvm.com
dodoma.shop
```

### IPs:
```
80.64.16.241
172.67.217.110
18.130.193.222
185.122.204.197
```

### Prozesse:
```
linuxsys
jailshell
sshd-agent (fake)
systemd-daemon (fake)
```

### Dateien:
```
/usr/bin/sshd-agent
/bin/systemd-daemon
/usr/local/bin/curl (fake)
/usr/local/rsyslo/rsyslo
/root/.systemd-utils/ntpclient
/root/Ongo-Manage/xmrig*
/root/c3pool/*
```

---

## How the Attack Worked

```
1. Initial Access (unknown - possibly SSH brute force or RCE)
         │
         ▼
2. Cronjob installed (runs every minute)
         │
         ▼
3. Downloads linux.sh from repositorylinux.xyz
         │
         ▼
4. linux.sh downloads linuxsys (XMRig) from GitHub/Pastebin/WordPress
         │
         ▼
5. linuxsys connects to cyberknull.publicvm.com:80
         │
         ▼
6. Mining Monero for the attacker
         │
         ▼
7. Self-healing: If any component dies, others restore it
```

---

## Cleanup Checklist

- [x] Kill all malicious processes
- [x] Remove malicious binaries
- [x] Delete malicious systemd services
- [x] Clean cronjobs
- [x] Replace fake curl with real curl
- [x] Remove /root/Ongo-Manage/xmrig*
- [x] Remove /root/c3pool/
- [x] Remove /root/.systemd-utils/
- [x] Change SSH credentials
- [x] Document everything

---

*Last updated: 2025-12-08*
