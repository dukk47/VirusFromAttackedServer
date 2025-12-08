# Abuse Reports - Vorlagen zum Melden

**Datum:** 2025-12-08
**Forensische Analyse:** https://github.com/dukk47/VirusFromAttackedServer

---

## Status Übersicht

| # | Empfänger | Status | Datum |
|---|-----------|--------|-------|
| 1 | GitHub | ✅ **GESENDET** | 2025-12-08 |
| 2 | Pastebin | ✅ **GESENDET** | 2025-12-08 |
| 3 | publicvm.com (Mining Proxy) | ✅ **GESENDET** | 2025-12-08 |
| 4 | Rumahweb (Domain Registrar) | ✅ **GESENDET** | 2025-12-08 |
| 5 | Polizei / LKA | 📝 Optional | - |
| 6 | Mining Pools | 📝 Optional | - |

---

## 1. GitHub - Account & Repositories melden

**URL:** https://github.com/contact/report-abuse
**Status:** ✅ **GESENDET** (2025-12-08)

**Betreff:** Malware distribution via GitHub repositories

**Report Text:**

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
**Status:** ✅ **GESENDET** (2025-12-08)

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

## 3. Hosting Provider - Mining Proxy melden

**Domain:** cyberknull.publicvm.com
**Service:** publicvm.com (free dynamic DNS)
**Status:** ✅ **GESENDET** (2025-12-08)

**Gesendete E-Mail:**

```
To the Abuse Department / Legal Team,

I am formally reporting a subdomain hosted on your infrastructure that is
actively being used as a critical component (Stratum mining proxy) for an
illegal cryptocurrency botnet.

NOTICE OF LIABILITY: By receiving this detailed report and forensic evidence,
you are now officially on notice regarding the criminal nature of this resource.
Continued hosting of cyberknull.publicvm.com following this notification
constitutes knowingly facilitating illegal cyber activities. Failure to suspend
this domain immediately may result in your organization being viewed as complicit
in the maintenance of this botnet infrastructure.

TARGET:

Domain: cyberknull.publicvm.com
Port: 80
Service: Stratum Mining Proxy (XMR/Monero)

TECHNICAL EVIDENCE:
Infected servers are forced to connect to this subdomain to mine cryptocurrency
for the attacker. Configuration extracted from infected hosts:

{
  "url": "cyberknull.publicvm.com:80",
  "pass": "lucifer"
}

FORENSIC ANALYSIS:
A complete forensic breakdown of the malware and the specific role of your
subdomain in this attack is available here:

Repository: https://github.com/dukk47/VirusFromAttackedServer
Reference: See c2-config/config.json and C2_INFRASTRUCTURE.md

ACTION REQUIRED:
Terminate this subdomain immediately to cease the active criminal activity
on your network.

Regards,
[Name]
```

---

## 4. Domain Registrar - repositorylinux.xyz melden

**Registrar:** CV. Rumahweb Indonesia
**Abuse E-Mail:** abuse@rumahweb.co.id
**Status:** ✅ **GESENDET** (2025-12-08)

**Betreff:** URGENT: Malware Distribution Domain - Immediate Action Required - repositorylinux.xyz

**Report Text:**

```
To the Abuse Department / Legal Team at Rumahweb,

I am formally reporting a domain registered through your service that is being
actively used as the PRIMARY DISTRIBUTION POINT for an international cryptocurrency
mining botnet.

NOTICE OF LIABILITY:
By receiving this detailed report with forensic evidence, you are now officially
on notice regarding the criminal nature of this domain. Continued registration of
repositorylinux.xyz following this notification constitutes knowingly facilitating
international cybercrime operations. Failure to suspend this domain immediately
may result in your organization being viewed as complicit in the maintenance of
this malware distribution infrastructure.

MALICIOUS DOMAIN: repositorylinux.xyz
REGISTRAR: CV. Rumahweb Indonesia (IANA ID: 1675)

CRITICAL THREAT DETAILS:

This domain hosts the PRIMARY DROPPER SCRIPT at:
https://repositorylinux.xyz/linux.sh

This script is executed via cronjob EVERY MINUTE on hundreds of infected servers
worldwide. It performs the following malicious actions:

1. Downloads and executes cryptocurrency mining malware (XMRig)
2. Installs multiple persistence mechanisms (cronjobs, systemd services)
3. Aggressively kills 150+ competing malware processes
4. Forces infected servers to mine Monero for the attacker
5. Deletes forensic evidence after execution

SCOPE OF ATTACK:
- Active botnet affecting servers globally
- Automated exploitation using vulnerability scanners
- Continuous reinfection every 60 seconds via cronjob
- Theft of computing resources worth thousands of dollars

FORENSIC EVIDENCE:
We have captured and documented the complete malware infrastructure:
https://github.com/dukk47/VirusFromAttackedServer

Key evidence files:
- linux_malware.sh.txt (complete dropper source code from your domain)
- ANALYSIS.md (full forensic breakdown)
- C2_INFRASTRUCTURE.md (command & control documentation)

LEGAL CONTEXT:
This domain is being used to commit violations of:
- Computer Fraud and Abuse Act (US)
- Computer Misuse Act (UK)
- § 202a-c, § 303a-b StGB (Germany)
- Similar cybercrime laws in all affected jurisdictions

ACTION REQUIRED:
Suspend this domain IMMEDIATELY to stop the ongoing criminal activity.

Every minute this domain remains active, additional servers are being compromised.

We expect confirmation of domain suspension within 24 hours.

Regards,
[Name]
```

---

## 5. Polizei / LKA - Strafanzeige (Optional)

**Zuständig:** LKA Cybercrime deines Bundeslandes
**Status:** 📝 Optional

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

**Status:** 📝 Optional

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

## Erwartete Wirkung

Alle kritischen Reports gesendet:

```
✅ GitHub     → Repos werden gelöscht, Account gesperrt
✅ Pastebin   → Fallback-Config offline
✅ publicvm   → Mining-Proxy tot
✅ Rumahweb   → Dropper-Domain offline

= Sein komplettes Botnet ist tot! 🎉
```

---

## Antworten Log

*(Hier Antworten dokumentieren wenn sie kommen)*

| Datum | Von | Antwort |
|-------|-----|---------|
| - | - | - |

---

*Erstellt: 2025-12-08*
*Letzte Aktualisierung: 2025-12-08*
