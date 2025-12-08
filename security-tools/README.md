# Security Tools

Sichere Tools zum Testen eigener Laravel-Anwendungen.

## laravel_security_check.py

Prüft Laravel-Apps auf bekannte Schwachstellen - **ohne Exploits oder Backdoors**.

### Was wird geprüft:

| Check | Beschreibung |
|-------|--------------|
| `.env` Exposure | Ist die .env Datei öffentlich erreichbar? |
| Debug Mode | Ist APP_DEBUG aktiviert? Debugbar/Telescope exposed? |
| Version Disclosure | Wird die Laravel-Version verraten? |
| RCE (CVE-2021-3129) | Ist die App anfällig für Remote Code Execution? |
| Common Issues | Log-Dateien, Git-Repos, Composer-Configs exposed? |

### Installation

```bash
pip install requests pycryptodome
```

### Nutzung

```bash
# Einzelne URL testen
python laravel_security_check.py https://deine-app.de

# Mehrere URLs aus Datei
python laravel_security_check.py urls.txt
```

### Beispiel-Output

```
[1/5] Checking .env exposure...
  ✗ VULNERABLE - .env file(s) exposed!
    - /.env
      ⚠ APP_KEY exposed!
      ⚠ Database credentials exposed!

[2/5] Checking debug mode...
  ✓ OK - No debug mode indicators

[3/5] Checking version disclosure...
  ✓ OK - No version disclosure

[4/5] Checking RCE vulnerability (CVE-2021-3129)...
  ✗ POTENTIALLY VULNERABLE to RCE!

[5/5] Checking common misconfigurations...
  ✗ Issues found:
    - /storage/logs/laravel.log: Log file exposed

RESULT: 3 potential issue(s) found!
```

### Fixes

Falls Schwachstellen gefunden werden:

**1. .env blockieren (Nginx):**
```nginx
location ~ /\.env {
    deny all;
    return 404;
}
```

**2. .env blockieren (Apache):**
```apache
<Files .env>
    Order allow,deny
    Deny from all
</Files>
```

**3. Debug Mode deaktivieren:**
```env
APP_DEBUG=false
APP_ENV=production
```

**4. Storage/Logs schützen:**
```nginx
location ~ ^/storage {
    deny all;
}
```

**5. APP_KEY rotieren:**
```bash
php artisan key:generate
```

---

## Wichtig

Diese Tools sind **nur für eigene Anwendungen** gedacht!
Unauthorized scanning ist illegal.
