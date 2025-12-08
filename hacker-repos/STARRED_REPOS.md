# Starred Repositories by whereveryouare666

Diese Repos hat der Angreifer gestarred - sie zeigen seine Tools und Techniken.

---

## 1. Laravel-RCE-Exploitation-Toolkit

**Repo:** https://github.com/khadafigans/Laravel-RCE-Exploitation-Toolkit
**Autor:** khadafigans
**Beschreibung:** Laravel Remote Code Execution Exploitation Toolkit

### Zweck:
Automatisiertes Ausnutzen von Laravel RCE Vulnerabilities (CVE-2021-3129 etc.)

### Wahrscheinliche Nutzung:
**HOCH** - Falls euer Server Laravel nutzt, war das vermutlich der Einstiegspunkt.

---

## 2. laravel-crypto-killer

**Repo:** https://github.com/synacktiv/laravel-crypto-killer
**Autor:** synacktiv (bekannte Security-Firma)
**Beschreibung:** "A tool designed to exploit bad implementations of decryption mechanisms in Laravel applications."

### Zweck:
Exploitet fehlerhafte Laravel Verschlüsselungs-Implementierungen

### Wahrscheinliche Nutzung:
Zum Knacken von Laravel APP_KEY oder Session Cookies

---

## 3. DataSurgeon

**Repo:** https://github.com/Drew-Alleman/DataSurgeon
**Autor:** Drew-Alleman
**Beschreibung:** "Quickly Extracts IP's, Email Addresses, Hashes, Files, Credit Cards, Social Security Numbers and a lot More From Text"

### Zweck:
Automatisierte Datenextraktion aus kompromittierten Systemen:
- IP-Adressen
- E-Mail-Adressen
- Passwort-Hashes
- Kreditkartennummern
- Sozialversicherungsnummern
- Dateien

### Wahrscheinliche Nutzung:
Reconnaissance und Post-Exploitation Datensammlung

---

## 4. lostfuzzer

**Repo:** https://github.com/coffinxp/lostfuzzer
**Autor:** coffinxp
**Beschreibung:** "A Bash script for automated nuclei dast scanning by using passive urls"

### Zweck:
Automatisiertes Vulnerability Scanning mit Nuclei

### Wahrscheinliche Nutzung:
Massenhaftes Scannen von Servern nach bekannten Vulnerabilities

---

## 5. nuclei-templates

**Repo:** https://github.com/coffinxp/nuclei-templates
**Autor:** coffinxp
**Beschreibung:** Custom Nuclei Templates für Vulnerability Scanning

### Zweck:
Erweitertes Vulnerability Scanning mit custom Templates

### Wahrscheinliche Nutzung:
Gezielte Scans nach spezifischen Schwachstellen

---

## Angriffskette basierend auf Starred Repos

```
1. RECONNAISSANCE
   └── DataSurgeon: Sammelt Infos über Ziele

2. SCANNING
   └── lostfuzzer + nuclei-templates: Findet Vulnerabilities

3. EXPLOITATION
   ├── Laravel-RCE-Exploitation-Toolkit: RCE auf Laravel
   └── laravel-crypto-killer: Knackt Laravel Crypto

4. POST-EXPLOITATION
   ├── 0xShell (eigenes Repo): Webshell für Zugang
   └── linuxsys (eigenes Repo): Cryptominer installieren
```

---

## Empfehlungen

### Falls ihr Laravel nutzt:
1. APP_KEY sofort rotieren
2. Laravel Version auf neueste updaten
3. Debug-Mode deaktivieren in Production
4. Alle CVEs für eure Version prüfen

### Generell:
1. Server auf DataSurgeon-Artefakte prüfen
2. Logs auf Nuclei/masscan Scans prüfen
3. Alle exponierten Services härten

---

*Dokumentiert: 2025-12-08*
