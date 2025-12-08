# Abuse Reports - Vorlagen zum Melden

**Datum:** 2025-12-08
**Forensische Analyse:** https://github.com/dukk47/VirusFromAttackedServer

---

## 1. GitHub - Account & Repositories melden

**URL:** https://github.com/contact/report-abuse

**Betreff:** Malware distribution via GitHub repositories

**Report Text (Copy & Paste):**

```
I am reporting malicious repositories used for cryptominer botnet distribution.

MALICIOUS USER:
- Username: whereveryouare666
- Profile: https://github.com/whereveryouare666
- User ID: 119106426

MALICIOUS REPOSITORIES:

1. https://github.com/whereveryouare666/linuxsys
   - Contains: XMRig cryptominer binaries (linux.bin, winsys.exe)
   - Contains: Mining configuration pointing to attacker's proxy
   - Used to: Automatically infect compromised Linux/Windows servers

2. https://github.com/whereveryouare666/0xShell
   - Contains: 27 PHP webshells for server exploitation
   - Description states: "Shell Bypass For All Server WAF"
   - Used to: Maintain unauthorized access to compromised servers

EVIDENCE:
Our server was compromised by this attacker. We have documented the complete
attack chain, malware samples, and C2 infrastructure in our forensic analysis:
https://github.com/dukk47/VirusFromAttackedServer

The attacker uses automated tools to scan for vulnerable servers, exploit them,
and deploy cryptominers that connect to their mining proxy at cyberknull.publicvm.com:80

IMPACT:
- Unauthorized cryptocurrency mining on victim servers
- Theft of computing resources
- Potential data theft via webshells
- Ongoing botnet operation affecting multiple victims

Please remove these repositories and suspend this account immediately.

Thank you.
```

---

## 2. Pastebin - Config-Fallback melden

**URL:** https://pastebin.com/report/5LRZX6XQ

**Report Text:**

```
This paste contains malware configuration for a cryptomining botnet.

Paste URL: https://pastebin.com/raw/5LRZX6XQ

Content: XMRig cryptocurrency miner configuration that connects to attacker's
mining proxy (cyberknull.publicvm.com:80). This is used as a fallback C2
configuration for infected servers.

This paste is part of an active botnet operation. Full forensic analysis
available at: https://github.com/dukk47/VirusFromAttackedServer

Please remove this paste.
```

---

## 3. Domain Registrar - repositorylinux.xyz melden

**Erst WHOIS prüfen:**
```bash
whois repositorylinux.xyz
```

**Dann Abuse-Mail an Registrar senden.**

**Betreff:** Malware distribution domain - repositorylinux.xyz

**Report Text:**

```
I am reporting a domain used for malware distribution.

MALICIOUS DOMAIN: repositorylinux.xyz

MALICIOUS URL: https://repositorylinux.xyz/linux.sh

PURPOSE:
This domain hosts a shell script dropper that:
1. Downloads cryptocurrency mining malware
2. Installs persistence mechanisms (cronjobs, systemd services)
3. Kills competing malware to ensure exclusive access
4. Connects to attacker's mining pool

The script is downloaded and executed via cronjob every minute on infected servers.

EVIDENCE:
Complete forensic analysis including the malware source code:
https://github.com/dukk47/VirusFromAttackedServer

Specifically see:
- linux_malware.sh.txt (the dropper script)
- ANALYSIS.md (forensic breakdown)

This domain is actively being used in ongoing attacks.
Please suspend this domain immediately.
```

---

## 4. Hosting Provider - Mining Proxy melden

**Domain:** cyberknull.publicvm.com
**Service:** publicvm.com (free dynamic DNS)

**URL:** Suche nach publicvm.com abuse contact

**Report Text:**

```
I am reporting a subdomain used as cryptocurrency mining proxy for a botnet.

MALICIOUS SUBDOMAIN: cyberknull.publicvm.com
PORT: 80

PURPOSE:
This subdomain is used as a Stratum mining proxy for a cryptomining botnet.
Infected servers connect to this address to mine Monero cryptocurrency
for the attacker.

Configuration found on infected servers:
{
  "url": "cyberknull.publicvm.com:80",
  "pass": "lucifer"
}

EVIDENCE:
Complete forensic analysis: https://github.com/dukk47/VirusFromAttackedServer
See: c2-config/config.json and C2_INFRASTRUCTURE.md

Please terminate this subdomain.
```

---

## 5. Polizei / LKA - Strafanzeige (Optional)

**Zuständig:** LKA Cybercrime deines Bundeslandes

**Online-Anzeige möglich in vielen Bundesländern:**
- NRW: https://polizei.nrw/internetwache
- Bayern: https://www.polizei.bayern.de/onlinewache
- etc.

**Straftatbestände:**
- § 202a StGB - Ausspähen von Daten
- § 202b StGB - Abfangen von Daten
- § 202c StGB - Vorbereiten des Ausspähens
- § 303a StGB - Datenveränderung
- § 303b StGB - Computersabotage

**Beweise mitliefern:**
- Link zu: https://github.com/dukk47/VirusFromAttackedServer
- Server-IP die gehackt wurde
- Zeitraum der Kompromittierung
- Entstandener Schaden (Stromkosten, Arbeitszeit, etc.)

---

## 6. Mining Pools informieren (Optional)

Falls die Wallet-Adressen noch aktiv sind:

**Hashvault:** support@hashvault.pro
**C3Pool:** Kontakt über deren Website

```
Wallet addresses used for illegal cryptomining botnet:

Hashvault:
88tGYBwhWNzGesQs5QkwE1PdBa1tXGb9dcjxrdwujU3SEs3i7psaoJc4KmrDvv4VPTNtXazDWGkvGGfqurdBggvPEhZ43DJ

C3Pool:
46d2vayVr8k8yH6YKLBsDsY8PNo2oqK7xeCiuECsLAsiTBiqNt6nkMPHQfi1vHTRzmAQyS9spDsnHcBnoeyxgVD1HLNNsLB

Evidence: https://github.com/dukk47/VirusFromAttackedServer
```

---

## Reihenfolge der Meldungen

1. **GitHub** (wichtigste - killt seine Repos)
2. **Pastebin** (Fallback weg)
3. **publicvm.com** (Mining-Proxy weg)
4. **Domain Registrar** (Dropper offline)
5. Polizei (optional, für Strafverfolgung)

**Nach 1-3 ist sein Botnet effektiv tot.**

---

*Erstellt: 2025-12-08*
