# Virus Samples from Attacked Server

Collected on: 2025-12-07

## Infection Summary

This server was heavily compromised with **multiple persistence mechanisms** that reinstall each other.

## Binaries

| File | Size | Location | Purpose |
|------|------|----------|---------|
| sshd-agent | 14MB | /usr/bin/sshd-agent | Main persistence trojan, restores cronjobs |
| systemd-daemon | 345KB | /bin/systemd-daemon | Secondary persistence |
| fake-curl | 3.4MB | /usr/local/bin/curl | Trojanized curl |
| rsyslo-binary | 1.4MB | /usr/local/rsyslo/rsyslo | Fake antivirus agent |

## Malicious Services (in /etc/systemd/system/)

| Service | Binary | Purpose |
|---------|--------|---------|
| sshd-agent.service | /usr/bin/sshd-agent | Persistence |
| systemd-agent.service | /bin/systemd-daemon | Persistence |
| alive.service | /tmp/runnv/alive.sh | Watchdog |
| lived.service | /tmp/runnv/lived.sh | Watchdog |
| networkerd.service | /tmp/runnv/runnv | Unknown |
| c3pool_miner.service | xmrig | Monero miner |
| system-update-service.service | xmrig | Monero miner (hashvault) |
| rsyslo.service | /usr/local/rsyslo/rsyslo | Fake AV |
| systemd-utils.service | ntpclient | Fake NTP client |

## Cronjob Persistence

Every minute downloads and executes:
- `https://repositorylinux.xyz/linux.sh`
- `http://80.64.16.241/unk.sh`

## C2 Infrastructure

- repositorylinux.xyz
- 80.64.16.241
- 172.67.217.110
- pool.hashvault.pro
- auto.c3pool.org

## Monero Wallets

- `88tGYBwhWNzGesQs5QkwE1PdBa1tXGb9dcjxrdwujU3SEs3i7psaoJc4KmrDvv4VPTNtXazDWGkvGGfqurdBggvPEhZ43DJ` (hashvault)
- `46d2vayVr8k8yH6YKLBsDsY8PNo2oqK7xeCiuECsLAsiTBiqNt6nkMPHQfi1vHTRzmAQyS9spDsnHcBnoeyxgVD1HLNNsLB` (c3pool)
