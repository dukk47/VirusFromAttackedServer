# Botnet Hashrate Tracker

Überwacht die C3Pool Mining-Wallet des Angreifers und zeichnet den Verlauf auf.

## Wallet
```
46d2vayVr8k8yH6YKLBsDsY8PNo2oqK7xeCiuECsLAsiTBiqNt6nkMPHQfi1vHTRzmAQyS9spDsnHcBnoeyxgVD1HLNNsLB
```

## Nutzung

```bash
# Einmal messen
./tracker.sh

# Kontinuierlich tracken (alle 5 Min)
./tracker.sh --loop

# Verlauf anzeigen
./tracker.sh --status
```

## Output

Die Daten werden in `hashrate_log.csv` gespeichert:

| Spalte | Beschreibung |
|--------|--------------|
| timestamp | Unix Timestamp |
| datetime | Lesbares Datum |
| hashrate_khs | Aktuelle Hashrate in KH/s |
| hashrate_avg_khs | Durchschnittliche Hashrate |
| valid_shares | Anzahl gültiger Shares |
| paid_xmr | Bereits ausgezahlte XMR |
| pending_xmr | Ausstehende XMR |

## Ziel

Dokumentieren wie das Botnet nach den Abuse-Reports stirbt.

---
*Erstellt: 2025-12-08*
