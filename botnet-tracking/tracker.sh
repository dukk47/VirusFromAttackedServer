#!/bin/bash

# ============================================
# BOTNET HASHRATE TRACKER
# ============================================
# Trackt die C3Pool Wallet des Angreifers
# Speichert Daten in CSV für spätere Analyse
#
# Nutzung:
#   ./tracker.sh              # Einmal ausführen
#   ./tracker.sh --loop       # Endlosschleife (alle 5 Min)
#   ./tracker.sh --status     # Aktuelle Stats anzeigen
# ============================================

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
WALLET="46d2vayVr8k8yH6YKLBsDsY8PNo2oqK7xeCiuECsLAsiTBiqNt6nkMPHQfi1vHTRzmAQyS9spDsnHcBnoeyxgVD1HLNNsLB"
LOGFILE="${SCRIPT_DIR}/hashrate_log.csv"
API_URL="https://api.c3pool.com/miner/${WALLET}/stats"
INTERVAL=300  # 5 Minuten

# Farben
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Header erstellen wenn Datei nicht existiert
init_log() {
    if [ ! -f "$LOGFILE" ]; then
        echo "timestamp,datetime,hashrate_khs,hashrate_avg_khs,valid_shares,paid_xmr,pending_xmr" > "$LOGFILE"
        echo -e "${GREEN}Log-Datei erstellt: ${LOGFILE}${NC}"
    fi
}

# Stats von API holen
fetch_stats() {
    STATS=$(curl -s --connect-timeout 10 "$API_URL" 2>/dev/null)

    if [ -z "$STATS" ] || echo "$STATS" | grep -q "error\|html"; then
        echo ""
        return 1
    fi

    echo "$STATS"
}

# Einen Datenpunkt loggen
log_datapoint() {
    STATS=$(fetch_stats)

    if [ -z "$STATS" ]; then
        echo -e "${RED}API Fehler - überspringe${NC}"
        return 1
    fi

    # Werte extrahieren
    HASHRATE=$(echo "$STATS" | python3 -c "import sys,json; d=json.load(sys.stdin); print(f\"{d['hash']/1000:.2f}\")" 2>/dev/null)
    HASHRATE_AVG=$(echo "$STATS" | python3 -c "import sys,json; d=json.load(sys.stdin); print(f\"{d['hash2']/1000:.2f}\")" 2>/dev/null)
    VALID_SHARES=$(echo "$STATS" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d['validShares'])" 2>/dev/null)
    PAID=$(echo "$STATS" | python3 -c "import sys,json; d=json.load(sys.stdin); print(f\"{d['amtPaid']/1e12:.6f}\")" 2>/dev/null)
    PENDING=$(echo "$STATS" | python3 -c "import sys,json; d=json.load(sys.stdin); print(f\"{d['amtDue']/1e12:.6f}\")" 2>/dev/null)

    TIMESTAMP=$(date +%s)
    DATETIME=$(date '+%Y-%m-%d %H:%M:%S')

    # In CSV speichern
    echo "${TIMESTAMP},${DATETIME},${HASHRATE},${HASHRATE_AVG},${VALID_SHARES},${PAID},${PENDING}" >> "$LOGFILE"

    # Ausgabe
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "  ${YELLOW}BOTNET TRACKER${NC} - ${DATETIME}"
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

    # Hashrate mit Farbe (grün wenn niedrig, rot wenn hoch)
    if (( $(echo "$HASHRATE < 100" | bc -l) )); then
        echo -e "  Hashrate:      ${GREEN}${HASHRATE} KH/s${NC} (Botnet stirbt!)"
    elif (( $(echo "$HASHRATE < 500" | bc -l) )); then
        echo -e "  Hashrate:      ${YELLOW}${HASHRATE} KH/s${NC}"
    else
        echo -e "  Hashrate:      ${RED}${HASHRATE} KH/s${NC}"
    fi

    echo -e "  Hashrate Avg:  ${HASHRATE_AVG} KH/s"
    echo -e "  Valid Shares:  ${VALID_SHARES}"
    echo -e "  ──────────────────────────────────────────────────"
    echo -e "  Ausgezahlt:    ${PAID} XMR"
    echo -e "  Ausstehend:    ${PENDING} XMR"
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

    # Anzahl Datenpunkte
    LINES=$(wc -l < "$LOGFILE" | tr -d ' ')
    echo -e "  ${GREEN}Datenpunkte gespeichert: $((LINES - 1))${NC}"
    echo ""
}

# Status anzeigen (Verlauf aus CSV)
show_status() {
    if [ ! -f "$LOGFILE" ]; then
        echo -e "${RED}Noch keine Daten vorhanden${NC}"
        exit 1
    fi

    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "  ${YELLOW}TRACKING VERLAUF${NC}"
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""

    # Header + letzte 20 Einträge
    echo -e "  Zeitpunkt             Hashrate     Avg       Pending XMR"
    echo -e "  ─────────────────────────────────────────────────────────"

    tail -20 "$LOGFILE" | while IFS=',' read -r ts dt hr hr_avg shares paid pending; do
        if [ "$ts" != "timestamp" ]; then
            printf "  %-20s %8s KH/s %8s KH/s  %s\n" "$dt" "$hr" "$hr_avg" "$pending"
        fi
    done

    echo ""

    # Statistik
    LINES=$(wc -l < "$LOGFILE" | tr -d ' ')
    FIRST_DATE=$(sed -n '2p' "$LOGFILE" | cut -d',' -f2)
    LAST_DATE=$(tail -1 "$LOGFILE" | cut -d',' -f2)

    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "  Datenpunkte:  $((LINES - 1))"
    echo -e "  Erster:       ${FIRST_DATE}"
    echo -e "  Letzter:      ${LAST_DATE}"
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
}

# Endlosschleife
run_loop() {
    echo -e "${GREEN}Starte Tracking (alle 5 Minuten)${NC}"
    echo -e "${YELLOW}Drücke Ctrl+C zum Beenden${NC}"
    echo ""

    while true; do
        log_datapoint
        echo -e "Nächste Messung in 5 Minuten..."
        sleep $INTERVAL
    done
}

# Main
init_log

case "$1" in
    --loop|-l)
        run_loop
        ;;
    --status|-s)
        show_status
        ;;
    *)
        log_datapoint
        echo -e "Tipp: ${YELLOW}./tracker.sh --loop${NC} für kontinuierliches Tracking"
        ;;
esac
