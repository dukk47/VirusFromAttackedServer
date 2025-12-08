# Komplettes Angreifer-Profil: whereveryouare666

## Account-Informationen

| Attribut | Wert |
|----------|------|
| **Username** | whereveryouare666 |
| **User ID** | 119106426 |
| **Profil URL** | https://github.com/whereveryouare666 |
| **Erstellt** | 26. November 2022 |
| **Letztes Update** | 25. November 2025 |
| **Follower** | 1 |
| **Following** | 14 |
| **Öffentliche Repos** | 2 |

---

## Seine Repositories

### 1. linuxsys (Cryptominer)
| Attribut | Wert |
|----------|------|
| **URL** | https://github.com/whereveryouare666/linuxsys |
| **Typ** | Original (nicht geforkt) |
| **Beschreibung** | Keine |
| **Inhalt** | XMRig Miner für Linux + Windows |

**Dateien:**
- `config.json` - Mining-Konfiguration
- `linux.bin` - Linux Miner (6.7 MB)
- `winsys.exe` - Windows Miner (7.9 MB)
- `nssm.exe` - Windows Service Manager

### 2. 0xShell (PHP Webshells)
| Attribut | Wert |
|----------|------|
| **URL** | https://github.com/whereveryouare666/0xShell |
| **Typ** | Fork |
| **Beschreibung** | "Shell Bypass For All Server WAF" |
| **Inhalt** | 27 PHP Webshells |

---

## Starred Repositories (Seine Tools)

### Exploitation Tools

| Repository | Autor | Beschreibung | Stars |
|------------|-------|--------------|-------|
| **Laravel-RCE-Exploitation-Toolkit** | khadafigans | Laravel Remote Code Execution Toolkit | 49 |
| **laravel-crypto-killer** | synacktiv | Exploitet schlechte Laravel Decryption | 117 |

### Reconnaissance & Data Extraction

| Repository | Autor | Beschreibung | Stars |
|------------|-------|--------------|-------|
| **DataSurgeon** | Drew-Alleman | Extrahiert IPs, Emails, Hashes, Kreditkarten, SSNs | 874 |

### Vulnerability Scanning

| Repository | Autor | Beschreibung | Stars |
|------------|-------|--------------|-------|
| **lostfuzzer** | coffinxp | Automatisiertes Nuclei DAST Scanning | 119 |
| **nuclei-templates** | coffinxp | Custom Vulnerability Scanner Templates | 449 |

---

## Following (14 Accounts)

Diese Accounts folgt der Angreifer - zeigt sein Netzwerk und Interessen:

### Security Researchers / Exploit Developers

| Username | Profil | Bekannt für |
|----------|--------|-------------|
| **ambionics** | https://github.com/ambionics | PHP/Laravel Exploits |
| **synacktiv** | (gestarred) | Security Research Firma |
| **horizon3ai** | https://github.com/horizon3ai | Exploit Development |
| **watchtowrlabs** | https://github.com/watchtowrlabs | Security Research |
| **assetnote** | https://github.com/assetnote | Bug Bounty / Research |

### Hacker / Tool Developers

| Username | Profil | Bekannt für |
|----------|--------|-------------|
| **coffinxp** | https://github.com/coffinxp | Nuclei Templates, lostfuzzer |
| **W01fh4cker** | https://github.com/W01fh4cker | Exploit Tools |
| **Chocapikk** | https://github.com/Chocapikk | Security Tools |
| **Nxploited** | https://github.com/Nxploited | Exploitation |
| **bigb0x** | https://github.com/bigb0x | Unknown |
| **dn9uy3n** | https://github.com/dn9uy3n | Unknown |
| **dwisiswant0** | https://github.com/dwisiswant0 | Security Tools |
| **KTN1990** | https://github.com/KTN1990 | Unknown |
| **h888t** | https://github.com/h888t | Unknown |
| **momika233** | https://github.com/momika233 | Unknown |

---

## Angriffskette (rekonstruiert)

Basierend auf seinen Tools und Repos:

```
┌─────────────────────────────────────────────────────────────┐
│  PHASE 1: RECONNAISSANCE                                     │
│                                                              │
│  Tools: DataSurgeon, lostfuzzer, nuclei-templates           │
│  Ziel: Server mit Laravel/PHP finden, Infos sammeln         │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│  PHASE 2: EXPLOITATION                                       │
│                                                              │
│  Tools: Laravel-RCE-Exploitation-Toolkit,                   │
│         laravel-crypto-killer                                │
│  Ziel: Remote Code Execution auf Laravel App                │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│  PHASE 3: PERSISTENCE                                        │
│                                                              │
│  Tools: 0xShell (27 PHP Webshells)                          │
│  Ziel: Dauerhafter Zugang via Webshell                      │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│  PHASE 4: MONETARISIERUNG                                    │
│                                                              │
│  Tools: linuxsys (XMRig), repositorylinux.xyz               │
│  Ziel: Monero Mining auf kompromittierten Servern           │
└─────────────────────────────────────────────────────────────┘
```

---

## Verbindungen zu anderen Akteuren

### Mögliche Zusammenarbeit:
- **coffinxp** - Nutzt dessen nuclei-templates
- **khadafigans** - Nutzt dessen Laravel-RCE-Toolkit

### Fork-Ursprung:
- **0xShell** wurde geforkt von **temempik1337**
  - Original: https://github.com/temempik1337/0xShell

---

## Indicators of Compromise (IOCs)

### GitHub-bezogen:
```
github.com/whereveryouare666
github.com/whereveryouare666/linuxsys
github.com/whereveryouare666/0xShell
User-ID: 119106426
```

### Netzwerk:
```
cyberknull.publicvm.com:80
repositorylinux.xyz
pastebin.com/raw/5LRZX6XQ
dodoma.shop
```

### Dateien:
```
linuxsys
linux.bin
winsys.exe
0xShell.php
config.json (mit "lucifer" password)
```

---

## Empfohlene Aktionen

### Melden:
1. **GitHub:** https://github.com/contact/report-abuse
   - User: whereveryouare666
   - Repos: linuxsys, 0xShell

2. **Pastebin:** https://pastebin.com/report
   - Paste: 5LRZX6XQ

### Blocken:
```
# Firewall-Regeln
iptables -A OUTPUT -d cyberknull.publicvm.com -j DROP
iptables -A OUTPUT -d repositorylinux.xyz -j DROP
```

### Prüfen:
- Laravel APP_KEY rotieren
- Alle PHP-Dateien auf Webshells scannen
- Server-Logs auf Nuclei/masscan Scans prüfen

---

*Profil erstellt: 2025-12-08*
*Letzte Aktualisierung: 2025-12-08*
