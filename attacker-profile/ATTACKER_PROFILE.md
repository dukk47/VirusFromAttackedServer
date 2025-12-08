# Attacker Profile: whereveryouare666

## GitHub Account

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

## Repositories des Angreifers

### 1. linuxsys (Cryptominer)

**URL:** https://github.com/whereveryouare666/linuxsys

| Datei | Größe | Zweck |
|-------|-------|-------|
| `config.json` | 1.3 KB | XMRig Mining-Konfiguration |
| `linux.bin` | 6.7 MB | Linux Miner Binary |
| `winsys.exe` | 7.9 MB | Windows Miner Binary |
| `nssm.exe` | 288 KB | Windows Service Manager (Persistenz) |

### 2. 0xShell (PHP Webshells)

**URL:** https://github.com/whereveryouare666/0xShell
**Beschreibung:** "Shell Bypass For All Server WAF"

**27 Webshell-Dateien:**
```
0x.php
0xObs.php
0xShell.php
0xShellObs.php
0xShellori.php
0xencbase.js
1337.php
_index.php
adminer.php       ← Datenbank-Admin-Tool
crot.php
f.php
f.txt
index.php
lndex.php         ← Typosquatting (l statt I)
log_update.php
login.php
logout.php
memek.php
root.php          ← Privilege Escalation
tifa.png.php      ← Getarnt als Bild
untitled.php
up.php            ← Upload-Funktionalität
weso.php
wesobase.js
wesoori.php
xoxo.php
```

---

## Starred Repositories (Interessen des Angreifers)

| Repository | Autor | Beschreibung |
|------------|-------|--------------|
| **laravel-crypto-killer** | synacktiv | Tool zum Ausnutzen schlechter Entschlüsselungs-Implementierungen in Laravel |
| **Laravel-RCE-Exploitation-Toolkit** | khadafigans | Laravel Remote Code Execution Toolkit |
| **DataSurgeon** | Drew-Alleman | Extrahiert IPs, E-Mails, Hashes, Kreditkarten, SSNs aus Text |
| **lostfuzzer** | coffinxp | Automatisiertes Nuclei DAST Scanning |
| **nuclei-templates** | coffinxp | Vulnerability Scanner Templates |

---

## Angreifer-Profil Zusammenfassung

### Fähigkeiten:
- Web Application Exploitation (Laravel, PHP)
- Cryptominer Deployment (XMRig)
- Cross-Platform Malware (Linux + Windows)
- WAF Bypass Techniken
- Automatisiertes Vulnerability Scanning

### Fokus:
- **Primär:** Cryptomining (Monero)
- **Sekundär:** Webserver-Kompromittierung via PHP Shells
- **Ziel:** Laravel/PHP-basierte Webapplikationen

### TTPs (Tactics, Techniques, Procedures):
1. Initiale Kompromittierung via Laravel RCE oder schwache Credentials
2. Webshell-Deployment für persistenten Zugang
3. Cryptominer-Installation via Dropper-Skript
4. Eigener Mining-Proxy zur Wallet-Verschleierung

---

## IOCs (Indicators of Compromise)

### GitHub:
```
github.com/whereveryouare666
github.com/whereveryouare666/linuxsys
github.com/whereveryouare666/0xShell
```

### Dateien:
```
linux.bin (SHA256 sollte erfasst werden)
winsys.exe
nssm.exe
0xShell.php
```

### Netzwerk:
```
cyberknull.publicvm.com:80
```

---

*Profil erstellt: 2025-12-08*
