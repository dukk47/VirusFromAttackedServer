# Fertige Abuse-E-Mails (Copy & Paste)

---

## 1. Domain Registrar: repositorylinux.xyz

**An:** abuse@rumahweb.co.id
**Betreff:** Abuse Report - Malware Distribution Domain: repositorylinux.xyz

```
Dear Rumahweb Abuse Team,

I am reporting a domain registered through your service that is being used
for malware distribution.

DOMAIN: repositorylinux.xyz

MALICIOUS ACTIVITY:
This domain hosts a malicious shell script at:
https://repositorylinux.xyz/linux.sh

This script is a cryptomining botnet dropper that:
1. Downloads and executes cryptocurrency mining malware
2. Installs persistence mechanisms (cronjobs, systemd services)
3. Kills competing malware processes
4. Connects infected servers to attacker's mining pool

The script is executed via cronjob every minute on infected servers worldwide.

EVIDENCE:
We have documented the complete attack including malware source code:
https://github.com/dukk47/VirusFromAttackedServer

Key files:
- linux_malware.sh.txt (the malicious dropper script)
- ANALYSIS.md (complete forensic analysis)

IMPACT:
- Unauthorized cryptocurrency mining on victim servers
- Theft of computing resources
- Active botnet affecting multiple victims globally

REQUEST:
Please suspend this domain immediately to stop ongoing attacks.

Thank you for your prompt attention to this matter.

Best regards,
[Dein Name]
```

---

## 2. Dynamic DNS Provider: publicvm.com (cyberknull.publicvm.com)

**Hinweis:** publicvm.com hat ein abgelaufenes SSL-Zertifikat - Seite nicht erreichbar.
**Alternative:** Suche nach "publicvm.com abuse" oder kontaktiere den Hoster der IP.

**IP von cyberknull.publicvm.com ermitteln:**
```bash
nslookup cyberknull.publicvm.com
```

**Dann WHOIS der IP prüfen für Abuse-Kontakt.**

**Falls Kontakt gefunden - E-Mail:**

**Betreff:** Abuse Report - Malicious Mining Proxy: cyberknull.publicvm.com

```
Dear Abuse Team,

I am reporting a subdomain/host being used as a cryptocurrency mining proxy
for a botnet operation.

HOST: cyberknull.publicvm.com
PORT: 80

MALICIOUS ACTIVITY:
This host operates a Stratum mining proxy that receives connections from
hundreds of infected servers worldwide. The infected servers mine Monero
cryptocurrency for the attacker.

Configuration found on compromised servers:
{
  "url": "cyberknull.publicvm.com:80",
  "pass": "lucifer",
  "tls": false
}

EVIDENCE:
Complete forensic analysis available at:
https://github.com/dukk47/VirusFromAttackedServer

See specifically:
- c2-config/config.json (mining configuration)
- C2_INFRASTRUCTURE.md (C2 documentation)

REQUEST:
Please terminate this subdomain/host to disrupt the botnet operation.

Thank you.

Best regards,
[Dein Name]
```

---

## 3. GitHub

**URL:** https://github.com/contact/report-abuse

**Abuse Type:** Malware or exploits

**Report (ins Formular einfügen):**

```
I am reporting malicious repositories used for cryptominer botnet distribution.

MALICIOUS USER:
- Username: whereveryouare666
- Profile: https://github.com/whereveryouare666
- User ID: 119106426

MALICIOUS REPOSITORIES:

1. https://github.com/whereveryouare666/linuxsys
   - Contains XMRig cryptominer binaries (linux.bin, winsys.exe)
   - Mining configuration connecting to attacker's proxy
   - Actively used to infect compromised servers

2. https://github.com/whereveryouare666/0xShell
   - Contains 27 PHP webshells for server exploitation
   - Description: "Shell Bypass For All Server WAF"
   - Used for unauthorized server access

EVIDENCE:
Our server was compromised. Complete forensic analysis:
https://github.com/dukk47/VirusFromAttackedServer

IMPACT:
- Active botnet operation
- Cryptocurrency mining on victim servers
- Potential data theft via webshells

Please remove these repositories and suspend this account.
```

---

## 4. Pastebin

**URL:** https://pastebin.com/report/5LRZX6XQ

**Report Reason:** Malware / Virus

**Details:**

```
This paste contains cryptocurrency mining botnet configuration.

URL: https://pastebin.com/raw/5LRZX6XQ

Content: XMRig miner configuration used as fallback C2 for infected servers.
Connects to attacker's mining proxy at cyberknull.publicvm.com:80

Evidence: https://github.com/dukk47/VirusFromAttackedServer

Please remove this paste.
```

---

## 5. Hashvault Mining Pool

**URL:** https://hashvault.pro (Support/Contact suchen)
**Oder:** support@hashvault.pro (falls existent)

**Betreff:** Abuse Report - Wallet used for illegal mining botnet

```
Dear Hashvault Team,

I am reporting a wallet address that is receiving cryptocurrency from
an illegal mining botnet.

WALLET ADDRESS:
88tGYBwhWNzGesQs5QkwE1PdBa1tXGb9dcjxrdwujU3SEs3i7psaoJc4KmrDvv4VPTNtXazDWGkvGGfqurdBggvPEhZ43DJ

MALICIOUS ACTIVITY:
This wallet receives Monero mined by a botnet that compromises servers
without authorization. The attacker uses automated tools to exploit
vulnerable servers and install XMRig miners.

EVIDENCE:
Complete forensic documentation:
https://github.com/dukk47/VirusFromAttackedServer

The configuration file (system-update-service.service) shows:
--url pool.hashvault.pro:443 --user [above wallet address]

REQUEST:
Please consider blocking this wallet from your pool.

Thank you.
```

---

## 6. C3Pool Mining Pool

**URL:** https://c3pool.com (Contact suchen)

**Betreff:** Abuse Report - Wallet used for illegal mining botnet

```
Dear C3Pool Team,

I am reporting a wallet address receiving cryptocurrency from illegal
botnet mining operations.

WALLET ADDRESS:
46d2vayVr8k8yH6YKLBsDsY8PNo2oqK7xeCiuECsLAsiTBiqNt6nkMPHQfi1vHTRzmAQyS9spDsnHcBnoeyxgVD1HLNNsLB

EVIDENCE:
Complete forensic documentation:
https://github.com/dukk47/VirusFromAttackedServer

See: services/c3pool_miner.service

REQUEST:
Please consider blocking this wallet.

Thank you.
```

---

## 7. Polizei / LKA Cybercrime (Optional)

**NRW:** https://polizei.nrw/internetwache
**Bayern:** https://www.polizei.bayern.de/onlinewache
**Andere Bundesländer:** Suche "Online Strafanzeige [Bundesland]"

**Straftatbestände:**
- § 202a StGB - Ausspähen von Daten
- § 303a StGB - Datenveränderung
- § 303b StGB - Computersabotage

**In der Anzeige angeben:**
- Server-IP: 217.154.86.217
- Zeitraum: Dezember 2025
- Schaden: Stromkosten, Arbeitszeit für Cleanup
- Beweise: https://github.com/dukk47/VirusFromAttackedServer
- Täter-Info: GitHub User whereveryouare666 (ID: 119106426)

---

## Zusammenfassung: Wem schicken?

| # | Empfänger | E-Mail / URL | Priorität |
|---|-----------|--------------|-----------|
| 1 | **GitHub** | https://github.com/contact/report-abuse | ⭐⭐⭐ HOCH |
| 2 | **Pastebin** | https://pastebin.com/report/5LRZX6XQ | ⭐⭐⭐ HOCH |
| 3 | **Rumahweb (Domain)** | abuse@rumahweb.co.id | ⭐⭐⭐ HOCH |
| 4 | **publicvm.com** | (IP WHOIS prüfen) | ⭐⭐ MITTEL |
| 5 | **Hashvault Pool** | Kontakt auf Website | ⭐ OPTIONAL |
| 6 | **C3Pool** | Kontakt auf Website | ⭐ OPTIONAL |
| 7 | **Polizei** | Online-Wache | ⭐ OPTIONAL |

**Die ersten 3 sind am wichtigsten - damit ist sein Botnet tot.**

---

*Erstellt: 2025-12-08*
