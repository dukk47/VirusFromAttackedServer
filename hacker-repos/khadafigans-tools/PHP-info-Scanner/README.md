# PHP Info / .env & Debug Leak Scanner

Fast multithreaded scanner to find **publicly exposed config and debug pages**:
- Laravel **`.env`** leaks
- **`phpinfo()`** pages
- Common **debug / profiler / toolbar** endpoints
- Parses responses to extract **API keys, creds, and service tokens** (AWS, Stripe, SMTP, Twilio/Nexmo, DB, cPanel, etc.)

> **Output is auto-organized** into a dated folder: `Results_YYYY-MM-DD-HH-MM/`

---

## ✨ Features
- 🔎 Targets common exposure endpoints (`.env`, `phpinfo`, debug/profiler pages)
- ⚡ Multithreaded for high throughput
- 🧠 Pattern extraction for popular secrets (AWS/Stripe/SMTP/DB and more)
- ♻️ **Session resume** via `.nero_swallowtail` (Ctrl+C → continue later)
- 🖼️ **Colored CLI** with your banner (pystyle gradient prompts)
- 📁 Auto-creates **dated** results folder

---

## 📦 Requirements
- Python **3.8+**
- Works on Windows / Linux / macOS

Install deps:
```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### 1) Quick start
```bash
python main.py
```
You’ll be prompted (with colored prompts) for:
- **List file** (e.g. `url.txt`) — one target per line, with or without scheme
- **Threads** (e.g. `10`)

### 2) Non-interactive (argv)
```bash
python main.py url.txt 10
```

### 3) Resume a previous run
- If you pressed **Ctrl+C** during scanning, a session file `.nero_swallowtail` was saved.
- On next run the tool will show:
  - `Session log found — restore`
  - Your prior `FILES`, `THREAD`, and last `SESSION` target
  - Prompt: **Continue session? [Y/n]**
- Choose **Y** to continue **from the next unprocessed target**.

---

## 🗂️ Inputs & Outputs

### Input list can be Work with only IP Address. No need to Reverse! (example)
```
https://example.com
http://target.tld
sub.domain.com
68.183.213.218
121.40.179.228
64.52.163.21
```

### Output directory
All results go to:
```
Results_YYYY-MM-DD-HH-MM/
```
Inside you’ll see files such as:
- `RESULT-AWS.txt` — extracted AWS keys
- `RESULT-STRIPE.txt` — Stripe keys found
- `RESULT-EMAIL.txt` — SMTP creds
- `RESULT-DB.txt` — DB creds / DSNs
- `Live_site.txt` — responsive/live sites
- plus other `RESULT-*` files depending on hits

> Filenames may vary slightly depending on which parsers get triggered by responses.

---

## ⚙️ What It Checks (high level)
- Laravel `.env` (common paths/variations)
- `phpinfo.php` & pages containing `phpinfo()` output
- Popular framework **debug/profiler** routes (e.g., toolbar/profiler dumps)
- Response parsing for API keys / creds:
  - **AWS**, **Stripe**, **Twilio/Nexmo**, **SMTP/Email**, **Database**, **cPanel**, etc.

> The scanner **does not exploit**; it fetches **public** endpoints and parses what the server returns.

---

## 🛠️ Troubleshooting

**Prompt not colored on some Windows terminals?**  
The tool prints gradient prompts with `pystyle`. If your terminal doesn’t render them, it automatically falls back to regular color (via `colorama`), or you can still type normally.

**`urllib3` compatibility**  
If you previously had errors with urllib3 2.x, the tool pins `urllib3==1.26.18` which works with `requests 2.31.x`.

**No session to restore**  
If there’s no `.nero_swallowtail` (or it lacks `[DB]`), the tool skips restore and goes straight to interactive prompts.

---

## ⚖️ Legal / Ethical
Use only on assets you **own** or are **authorized** to test. You are responsible for complying with all applicable laws and program rules. The authors and contributors are not liable for misuse.

---

📧 Contact :
------
Join My Channel to discover all of my tools. Add Me On : 
```
[+] Telegram : @marleyybob123
[+] Telegram Channel : https://t.me/BMARLEYTOOLS
```

---

## 💬 Credits
- CLI coloring: `pystyle`, `colorama`
- HTTP: `requests` / `urllib3`
- Thanks to @DesordenHackitivision for the original source code & workflow direction.

👨‍💻 Author: Bob Marley
------
Buy me a Coffe :
```
If you find this project useful and want to support future development:

₿  BTC: 17sbbeTzDMP4aMELVbLW78Rcsj4CDRBiZh
₮  USDT: TQfx5kjY4d1Q6piDgBVL31d8YJ8xCx5uTd (TRC-20)
Ξ  ETH: 0xb88cdeba793e13fa39ee19ad34cfe69916b81fa0 (ERC-20)
Ł  LTC: LffRsEacPDGmFGQESpnSSRTECRxXq4txPq
```
<br>©2025 Bob Marley
