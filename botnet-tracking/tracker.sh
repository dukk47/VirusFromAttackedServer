#!/bin/bash

# ============================================
# BOTNET HASHRATE TRACKER
# ============================================
# Trackt die C3Pool Wallet des Angreifers
# Holt automatisch historische Daten von der API
#
# Nutzung:
#   ./tracker.sh              # Aktuelle Stats + History sync
#   ./tracker.sh --loop       # Endlosschleife (alle 5 Min)
#   ./tracker.sh --status     # Verlauf anzeigen
#   ./tracker.sh --graph      # ASCII Graph
# ============================================

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
WALLET="46d2vayVr8k8yH6YKLBsDsY8PNo2oqK7xeCiuECsLAsiTBiqNt6nkMPHQfi1vHTRzmAQyS9spDsnHcBnoeyxgVD1HLNNsLB"
LOGFILE="${SCRIPT_DIR}/hashrate_log.csv"
API_STATS="https://api.c3pool.com/miner/${WALLET}/stats"
API_HISTORY="https://api.c3pool.com/miner/${WALLET}/chart/hashrate"
INTERVAL=300  # 5 Minuten

# Farben
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

# Header erstellen wenn Datei nicht existiert
init_log() {
    if [ ! -f "$LOGFILE" ]; then
        echo "timestamp,datetime,hashrate_khs,hashrate_avg_khs,paid_xmr,pending_xmr" > "$LOGFILE"
        echo -e "${GREEN}Log-Datei erstellt${NC}"
    fi
}

# Historische Daten von API holen und in CSV einfügen
sync_history() {
    echo -e "${YELLOW}Synchronisiere historische Daten von C3Pool...${NC}"

    # Letzten Timestamp aus CSV holen (falls vorhanden)
    if [ -f "$LOGFILE" ] && [ $(wc -l < "$LOGFILE") -gt 1 ]; then
        LAST_TS=$(tail -1 "$LOGFILE" | cut -d',' -f1)
    else
        LAST_TS=0
    fi

    # History von API holen und neue Einträge hinzufügen
    curl -s "$API_HISTORY" 2>/dev/null | python3 -c "
import json, sys
from datetime import datetime

try:
    data = json.load(sys.stdin)
except:
    sys.exit(1)

last_ts = int(${LAST_TS})
new_entries = 0

# Sortiere nach Zeit (älteste zuerst)
data.sort(key=lambda x: x['ts'])

for entry in data:
    ts = int(entry['ts'] / 1000)  # ms to seconds

    # Nur neue Einträge (und nur alle 10 Min um Datenmenge zu reduzieren)
    if ts > last_ts:
        dt = datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        hs = entry['hs'] / 1000
        hs2 = entry['hs2'] / 1000
        # paid/pending nicht in history, setze 0
        print(f'{ts},{dt},{hs:.2f},{hs2:.2f},0,0')
        new_entries += 1
        last_ts = ts

# Info ausgeben
sys.stderr.write(f'{new_entries}')
" >> "$LOGFILE" 2>/tmp/sync_count

    COUNT=$(cat /tmp/sync_count 2>/dev/null || echo "0")
    if [ "$COUNT" != "0" ]; then
        echo -e "${GREEN}${COUNT} neue Datenpunkte hinzugefügt${NC}"
    else
        echo -e "${CYAN}Bereits synchron${NC}"
    fi
}

# Aktuelle Stats holen und loggen
log_current() {
    STATS=$(curl -s --connect-timeout 10 "$API_STATS" 2>/dev/null)

    if [ -z "$STATS" ] || echo "$STATS" | grep -q "error\|html"; then
        echo -e "${RED}API Fehler${NC}"
        return 1
    fi

    # Werte extrahieren
    read HASHRATE HASHRATE_AVG PAID PENDING <<< $(echo "$STATS" | python3 -c "
import sys,json
d=json.load(sys.stdin)
print(f\"{d['hash']/1000:.2f} {d['hash2']/1000:.2f} {d['amtPaid']/1e12:.6f} {d['amtDue']/1e12:.6f}\")
" 2>/dev/null)

    TIMESTAMP=$(date +%s)
    DATETIME=$(date '+%Y-%m-%d %H:%M:%S')

    # In CSV speichern
    echo "${TIMESTAMP},${DATETIME},${HASHRATE},${HASHRATE_AVG},${PAID},${PENDING}" >> "$LOGFILE"

    # Ausgabe
    echo ""
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "  ${BOLD}BOTNET TRACKER${NC} - ${DATETIME}"
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

    # Hashrate mit Farbe
    if (( $(echo "$HASHRATE < 100" | bc -l) )); then
        echo -e "  Hashrate:      ${GREEN}${HASHRATE} KH/s${NC} (fast tot!)"
    elif (( $(echo "$HASHRATE < 300" | bc -l) )); then
        echo -e "  Hashrate:      ${GREEN}${HASHRATE} KH/s${NC} (sinkt!)"
    elif (( $(echo "$HASHRATE < 600" | bc -l) )); then
        echo -e "  Hashrate:      ${YELLOW}${HASHRATE} KH/s${NC}"
    else
        echo -e "  Hashrate:      ${RED}${HASHRATE} KH/s${NC}"
    fi

    echo -e "  Durchschnitt:  ${HASHRATE_AVG} KH/s"
    echo -e "  ──────────────────────────────────────────────────"
    echo -e "  Ausgezahlt:    ${PAID} XMR"
    echo -e "  Ausstehend:    ${PENDING} XMR"
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
}

# ASCII Graph anzeigen
show_graph() {
    if [ ! -f "$LOGFILE" ] || [ $(wc -l < "$LOGFILE") -lt 3 ]; then
        echo -e "${RED}Nicht genug Daten für Graph${NC}"
        return 1
    fi

    echo ""
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "  ${BOLD}HASHRATE VERLAUF${NC}"
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""

    python3 << 'PYTHON'
import csv
from datetime import datetime
from collections import defaultdict

# Daten laden
data = []
with open('hashrate_log.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        try:
            ts = int(row['timestamp'])
            hr = float(row['hashrate_khs'])
            data.append((ts, hr))
        except:
            pass

if not data:
    print("  Keine Daten")
    exit()

# Nach Stunden gruppieren
hourly = defaultdict(list)
for ts, hr in data:
    hour = datetime.fromtimestamp(ts).strftime('%m-%d %H:00')
    hourly[hour].append(hr)

# Durchschnitt pro Stunde
hourly_avg = {h: sum(v)/len(v) for h, v in hourly.items()}

# Sortiert ausgeben
hours = sorted(hourly_avg.keys())[-48:]  # Letzte 48 Stunden max
max_hr = max(hourly_avg.values()) if hourly_avg else 1

# Graph zeichnen
width = 50
for hour in hours:
    hr = hourly_avg[hour]
    bar_len = int((hr / max_hr) * width)
    bar = '█' * bar_len

    # Farbe basierend auf Hashrate
    if hr < 100:
        color = '\033[0;32m'  # grün
    elif hr < 400:
        color = '\033[1;33m'  # gelb
    else:
        color = '\033[0;31m'  # rot

    print(f"  {hour} │{color}{bar}\033[0m {hr:.0f} KH/s")

# Statistik
print("")
print(f"  ────────────────────────────────────────────────────────────────────")
first_hr = data[0][1] if data else 0
last_hr = data[-1][1] if data else 0
max_val = max(d[1] for d in data)
min_val = min(d[1] for d in data)
change = ((last_hr - first_hr) / first_hr * 100) if first_hr > 0 else 0

print(f"  Peak:     {max_val:.0f} KH/s")
print(f"  Minimum:  {min_val:.0f} KH/s")
print(f"  Aktuell:  {last_hr:.0f} KH/s")
if change < 0:
    print(f"  Trend:    \033[0;32m{change:.1f}%\033[0m (Botnet schrumpft!)")
else:
    print(f"  Trend:    \033[0;31m+{change:.1f}%\033[0m")
PYTHON

    echo ""
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
}

# Status anzeigen
show_status() {
    if [ ! -f "$LOGFILE" ]; then
        echo -e "${RED}Noch keine Daten${NC}"
        exit 1
    fi

    echo ""
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "  ${BOLD}LETZTE MESSUNGEN${NC}"
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    echo -e "  Zeitpunkt              Hashrate      Avg"
    echo -e "  ─────────────────────────────────────────────────────────"

    tail -20 "$LOGFILE" | while IFS=',' read -r ts dt hr hr_avg paid pending; do
        if [ "$ts" != "timestamp" ]; then
            printf "  %-21s %8s KH/s  %8s KH/s\n" "$dt" "$hr" "$hr_avg"
        fi
    done

    echo ""
    LINES=$(($(wc -l < "$LOGFILE") - 1))
    echo -e "  ${GREEN}Gesamt: ${LINES} Datenpunkte${NC}"
    echo ""
}

# Endlosschleife
run_loop() {
    echo -e "${GREEN}Starte Tracking (alle 5 Minuten)${NC}"
    echo -e "${YELLOW}Drücke Ctrl+C zum Beenden${NC}"

    while true; do
        log_current
        echo ""
        echo -e "  Nächste Messung in 5 Minuten..."
        sleep $INTERVAL
    done
}

# Main
init_log

case "$1" in
    --loop|-l)
        sync_history
        run_loop
        ;;
    --status|-s)
        show_status
        ;;
    --graph|-g)
        show_graph
        ;;
    --sync)
        sync_history
        ;;
    *)
        sync_history
        log_current
        echo ""
        echo -e "  ${YELLOW}Befehle:${NC}"
        echo -e "    ./tracker.sh --loop    Kontinuierlich tracken"
        echo -e "    ./tracker.sh --graph   ASCII Graph anzeigen"
        echo -e "    ./tracker.sh --status  Letzte Messungen"
        echo ""
        ;;
esac
