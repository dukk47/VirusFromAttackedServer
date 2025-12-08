# C2 (Command & Control) Infrastruktur

## Übersicht

Das Botnet verwendet ein **Pull-basiertes C2-System** - keine direkte Verbindung zum Angreifer, sondern regelmäßiges Abrufen von Konfigurationsdateien.

---

## Architektur

```
┌─────────────────────────────────────────────────────────────┐
│                      ANGREIFER                               │
│            (ändert config.json auf GitHub)                   │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                  CONFIG SERVER (C2)                          │
│                                                              │
│   Primär:   github.com/whereveryouare666/linuxsys           │
│   Fallback: pastebin.com/raw/5LRZX6XQ                       │
│   Fallback: dodoma.shop (gehackte WordPress-Seite)          │
└─────────────────────────┬───────────────────────────────────┘
                          │
                    alle 60 Sekunden
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                    INFIZIERTE BOTS                           │
│                                                              │
│   - Laden config.json herunter                              │
│   - watch: true → automatische Übernahme neuer Configs      │
│   - Verbinden sich zum Mining-Pool                          │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                   MINING PROXY                               │
│                                                              │
│   cyberknull.publicvm.com:80                                │
│   (eigener Stratum-Proxy des Angreifers)                    │
│                                                              │
│   → Aggregiert Mining-Ergebnisse aller Bots                 │
│   → Wallet ist auf dem Proxy konfiguriert                   │
└─────────────────────────────────────────────────────────────┘
```

---

## C2-Endpunkte

### Primärer C2: GitHub

| URL | Zweck |
|-----|-------|
| `https://raw.githubusercontent.com/whereveryouare666/linuxsys/refs/heads/main/config.json` | Mining-Konfiguration |
| `https://raw.githubusercontent.com/whereveryouare666/linuxsys/refs/heads/main/linux.bin` | Linux Payload |

**Vorteile für den Angreifer:**
- GitHub ist selten von Firewalls blockiert
- Kostenlos und zuverlässig
- Einfache Updates via Git Commit

### Fallback C2: Pastebin

| URL | Zweck |
|-----|-------|
| `https://pastebin.com/raw/5LRZX6XQ` | Backup-Konfiguration |

### Fallback C2: Gehackte WordPress-Seite

| URL | Zweck |
|-----|-------|
| `https://dodoma.shop/wp-content/uploads/2000/01/linux.bin` | Backup-Payload |

**Beobachtung:** Der Pfad `/wp-content/uploads/2000/01/` suggeriert ein Datum aus dem Jahr 2000 - absichtlich unplausibel zur Verschleierung.

---

## Mining-Pool (Stratum Proxy)

### Hauptpool:

| Attribut | Wert |
|----------|------|
| **URL** | `cyberknull.publicvm.com:80` |
| **Port** | 80 (HTTP - Firewall-Umgehung) |
| **Passwort** | `lucifer` |
| **TLS** | Nein (unverschlüsselt) |
| **Protokoll** | Stratum |

### Warum Port 80?
- HTTP-Traffic wird von Firewalls selten blockiert
- Sieht aus wie normaler Web-Traffic
- Viele Unternehmen erlauben Outbound Port 80

### Warum eigener Proxy?
- Keine Wallet-Adresse in der Config nötig
- Wallet ist auf dem Proxy konfiguriert
- Ermöglicht Aggregation aller Bot-Mining-Ergebnisse
- Einfacher Pool-Wechsel ohne Client-Update

---

## Steuerungsmechanismus

### Wie der Angreifer Befehle sendet:

Der Angreifer muss **keine direkte Verbindung** zu den Bots haben. Stattdessen:

1. **Config ändern auf GitHub** → Alle Bots laden neue Config
2. **watch: true** → XMRig übernimmt Änderungen automatisch
3. **health-print-time: 60** → Alle 60 Sekunden Health-Check

### Mögliche Befehle durch Config-Änderung:

| Aktion | Config-Änderung |
|--------|-----------------|
| Pool wechseln | `pools[0].url` ändern |
| Mining stoppen | `cpu.enabled: false` |
| Intensität ändern | `max-threads-hint` anpassen |
| Zu neuem Server migrieren | Neue Pool-URL |

---

## Bekannte C2-Domains/IPs

### Aktive C2:
```
cyberknull.publicvm.com:80     (Mining Proxy)
raw.githubusercontent.com       (Config/Payload)
pastebin.com                    (Fallback Config)
dodoma.shop                     (Fallback Payload)
repositorylinux.xyz             (Dropper Script)
```

### IPs in der Kill-Liste (vermutlich konkurrierende C2):
```
18.130.193.222      (AWS EU-West-2)
185.122.204.197     (Mining-Pool)
205.147.101.*       (IP-Range)
80.64.16.241        (Backup Dropper - offline)
```

---

## Timeline der Angreifer-Aktivität

| Datum | Aktion |
|-------|--------|
| 26. Nov 2022 | GitHub-Account erstellt |
| 28. Jun 2025 | Repository `linuxsys` erstellt |
| 31. Okt 2025 | config.json hinzugefügt |
| 22. Nov 2025 | config.json aktualisiert |
| 07. Dez 2025 | Zwei Updates (04:40 + 04:42 Uhr) |
| 07. Dez 2025 | **Euer Server kompromittiert** |

---

## Erkennung

### Netzwerk-Monitoring:

```bash
# Verbindungen zum Mining-Proxy
netstat -an | grep "publicvm.com\|:80"

# DNS-Anfragen
tcpdump -i any port 53 | grep -E "publicvm|cyberknull"

# Stratum-Protokoll auf Port 80
tcpdump -i any port 80 | grep -i "mining\|stratum"
```

### Firewall-Regeln:

```bash
# Blockieren
iptables -A OUTPUT -d cyberknull.publicvm.com -j DROP
iptables -A OUTPUT -p tcp --dport 80 -m string --string "stratum" --algo bm -j DROP
```

---

*Dokumentation erstellt: 2025-12-08*
