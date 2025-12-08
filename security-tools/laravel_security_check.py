#!/usr/bin/env python3
"""
Laravel Security Checker
========================
Prüft Laravel-Anwendungen auf bekannte Schwachstellen.
KEINE Backdoors, KEIN Exploit - nur Detection.

Checks:
1. Exposed .env file
2. APP_DEBUG enabled
3. APP_KEY leaked
4. Laravel version disclosure
5. RCE vulnerability (CVE-2021-3129)

Nutzung:
    python laravel_security_check.py https://deine-app.de
    python laravel_security_check.py urls.txt

Autor: Security Check Tool (Safe Version)
"""

import sys
import re
import json
import base64
import hmac
import requests
from hashlib import sha256
from urllib.parse import urljoin
from datetime import datetime

# Suppress SSL warnings
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Farben für Terminal
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    END = '\033[0m'

def banner():
    print(f"""
{Colors.CYAN}╔═══════════════════════════════════════════════════════════╗
║  {Colors.BOLD}Laravel Security Checker{Colors.END}{Colors.CYAN}                                 ║
║  Safe vulnerability detection - no exploits, no backdoors  ║
╚═══════════════════════════════════════════════════════════╝{Colors.END}
""")

def check_env_exposed(url):
    """Check if .env file is publicly accessible"""
    env_paths = ['/.env', '/.env.backup', '/.env.old', '/.env.save', '/.env.example']
    results = []

    for path in env_paths:
        try:
            resp = requests.get(urljoin(url, path), timeout=10, verify=False,
                              headers={'User-Agent': 'Mozilla/5.0 Security-Check'})
            if resp.status_code == 200:
                # Check if it looks like a real .env file
                if 'APP_KEY=' in resp.text or 'DB_PASSWORD=' in resp.text:
                    results.append({
                        'path': path,
                        'status': 'VULNERABLE',
                        'has_app_key': 'APP_KEY=' in resp.text,
                        'has_db_creds': 'DB_PASSWORD=' in resp.text or 'DB_USERNAME=' in resp.text,
                        'has_mail_creds': 'MAIL_PASSWORD=' in resp.text,
                        'content_preview': resp.text[:500] if len(resp.text) < 1000 else '[TRUNCATED - Full .env exposed!]'
                    })
        except:
            pass

    return results

def extract_app_key(env_content):
    """Extract APP_KEY from .env content"""
    match = re.search(r'APP_KEY\s*=\s*([^\s\n]+)', env_content)
    if match:
        return match.group(1)
    return None

def check_debug_mode(url):
    """Check if APP_DEBUG is enabled by triggering an error"""
    debug_indicators = []

    # Try to trigger a Laravel error page
    test_urls = [
        urljoin(url, '/_debugbar'),
        urljoin(url, '/telescope'),
        urljoin(url, '/__clockwork'),
        urljoin(url, '/api/nonexistent-endpoint-test-12345'),
    ]

    for test_url in test_urls:
        try:
            resp = requests.get(test_url, timeout=10, verify=False,
                              headers={'User-Agent': 'Mozilla/5.0 Security-Check'})

            # Check for debug indicators
            if 'Whoops!' in resp.text or 'Stack trace' in resp.text:
                debug_indicators.append('Whoops error page exposed')
            if 'Laravel Debugbar' in resp.text or '_debugbar' in resp.text:
                debug_indicators.append('Laravel Debugbar enabled')
            if 'Laravel Telescope' in resp.text:
                debug_indicators.append('Laravel Telescope exposed')
            if 'clockwork' in resp.text.lower() and resp.status_code == 200:
                debug_indicators.append('Clockwork debug tool exposed')
            if 'APP_DEBUG' in resp.text:
                debug_indicators.append('APP_DEBUG visible in error')
            if 'base_path' in resp.text or 'vendor/laravel' in resp.text:
                debug_indicators.append('Server paths exposed in error')

        except:
            pass

    return list(set(debug_indicators))

def check_laravel_version(url):
    """Try to detect Laravel version"""
    version_info = {}

    try:
        # Check common version disclosure points
        resp = requests.get(url, timeout=10, verify=False,
                          headers={'User-Agent': 'Mozilla/5.0 Security-Check'})

        # X-Powered-By header
        if 'X-Powered-By' in resp.headers:
            version_info['x_powered_by'] = resp.headers['X-Powered-By']

        # Laravel specific headers
        if 'X-Laravel' in resp.headers:
            version_info['laravel_header'] = resp.headers['X-Laravel']

        # Check for version in HTML comments or meta tags
        version_match = re.search(r'laravel[\/\s]*v?(\d+\.\d+(?:\.\d+)?)', resp.text, re.I)
        if version_match:
            version_info['detected_version'] = version_match.group(1)

    except:
        pass

    return version_info

def check_rce_vulnerable(url, app_key):
    """
    Check if Laravel is vulnerable to CVE-2021-3129 (Ignition RCE)
    SAFE CHECK - only sends a harmless test payload, no actual exploit
    """
    if not app_key or not app_key.startswith('base64:'):
        return {'vulnerable': False, 'reason': 'No valid APP_KEY to test'}

    try:
        # Decode the key
        key = base64.b64decode(app_key.replace('base64:', ''))

        # Create a SAFE test payload that just echoes a string (no file writes, no code exec)
        # This payload is intentionally broken/safe - it won't execute anything harmful
        test_marker = f"SECURITY_CHECK_{datetime.now().strftime('%Y%m%d%H%M%S')}"

        # Create minimal serialized object that would trigger deserialization
        # but with harmless content (just returns a string)
        safe_payload = f'O:8:"stdClass":1:{{s:4:"test";s:{len(test_marker)}:"{test_marker}";}}'

        # Encrypt it Laravel-style
        from Crypto.Cipher import AES
        from Crypto.Random import get_random_bytes
        from Crypto.Util.Padding import pad

        iv = get_random_bytes(16)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        encoded = base64.b64encode(safe_payload.encode()).decode()
        value = cipher.encrypt(pad(base64.b64decode(encoded), AES.block_size))
        payload_b64 = base64.b64encode(value)
        iv_b64 = base64.b64encode(iv)
        mac = hmac.new(key, iv_b64 + payload_b64, sha256).hexdigest()

        cookie_data = json.dumps({
            'iv': iv_b64.decode(),
            'value': payload_b64.decode(),
            'mac': mac
        })
        cookie_value = base64.b64encode(cookie_data.encode()).decode()

        # Send request with crafted cookie
        resp = requests.get(
            url,
            cookies={'laravel_session': cookie_value},
            timeout=10,
            verify=False,
            headers={'User-Agent': 'Mozilla/5.0 Security-Check'}
        )

        # Check response for signs of deserialization attempt
        # A vulnerable server might show errors about unserialize or class not found
        vuln_indicators = [
            'unserialize',
            'Illuminate\\',
            '__wakeup',
            '__destruct',
            'allowed_classes'
        ]

        for indicator in vuln_indicators:
            if indicator in resp.text:
                return {
                    'vulnerable': True,
                    'indicator': indicator,
                    'reason': 'Server attempted to deserialize payload'
                }

        return {
            'vulnerable': False,
            'reason': 'No deserialization indicators found'
        }

    except ImportError:
        return {
            'vulnerable': 'UNKNOWN',
            'reason': 'pycryptodome not installed (pip install pycryptodome)'
        }
    except Exception as e:
        return {
            'vulnerable': 'ERROR',
            'reason': str(e)
        }

def check_common_vulnerabilities(url):
    """Check for other common Laravel misconfigurations"""
    issues = []

    paths_to_check = [
        ('/storage/logs/laravel.log', 'Log file exposed'),
        ('/storage/framework/sessions', 'Session directory exposed'),
        ('/vendor/autoload.php', 'Vendor directory exposed'),
        ('/.git/config', 'Git repository exposed'),
        ('/composer.json', 'Composer config exposed'),
        ('/composer.lock', 'Composer lock exposed'),
        ('/phpinfo.php', 'phpinfo() exposed'),
        ('/info.php', 'PHP info exposed'),
        ('/.htaccess', '.htaccess readable'),
        ('/web.config', 'web.config readable'),
    ]

    for path, description in paths_to_check:
        try:
            resp = requests.get(urljoin(url, path), timeout=5, verify=False,
                              headers={'User-Agent': 'Mozilla/5.0 Security-Check'})
            if resp.status_code == 200 and len(resp.text) > 10:
                # Verify it's actually the file content, not a custom 404
                if path.endswith('.log') and ('[' in resp.text and ']' in resp.text):
                    issues.append({'path': path, 'issue': description})
                elif path.endswith('.json') and '{' in resp.text:
                    issues.append({'path': path, 'issue': description})
                elif '.git' in path and '[core]' in resp.text:
                    issues.append({'path': path, 'issue': description})
                elif 'phpinfo' in path and 'PHP Version' in resp.text:
                    issues.append({'path': path, 'issue': description})
        except:
            pass

    return issues

def scan_url(url):
    """Run all security checks on a URL"""
    if not url.startswith('http'):
        url = 'https://' + url

    url = url.rstrip('/')

    print(f"\n{Colors.BLUE}{'='*60}{Colors.END}")
    print(f"{Colors.BOLD}Scanning: {url}{Colors.END}")
    print(f"{Colors.BLUE}{'='*60}{Colors.END}\n")

    results = {
        'url': url,
        'timestamp': datetime.now().isoformat(),
        'checks': {}
    }

    # 1. Check .env exposure
    print(f"{Colors.CYAN}[1/5] Checking .env exposure...{Colors.END}")
    env_results = check_env_exposed(url)
    if env_results:
        print(f"  {Colors.RED}✗ VULNERABLE - .env file(s) exposed!{Colors.END}")
        for r in env_results:
            print(f"    - {r['path']}")
            if r.get('has_app_key'):
                print(f"      {Colors.RED}⚠ APP_KEY exposed!{Colors.END}")
            if r.get('has_db_creds'):
                print(f"      {Colors.RED}⚠ Database credentials exposed!{Colors.END}")
        results['checks']['env_exposed'] = env_results

        # Extract APP_KEY for further testing
        app_key = None
        for r in env_results:
            if 'content_preview' in r:
                try:
                    resp = requests.get(urljoin(url, r['path']), timeout=10, verify=False)
                    app_key = extract_app_key(resp.text)
                    if app_key:
                        print(f"      {Colors.YELLOW}APP_KEY: {app_key[:20]}...{Colors.END}")
                        break
                except:
                    pass
    else:
        print(f"  {Colors.GREEN}✓ OK - .env not publicly accessible{Colors.END}")
        results['checks']['env_exposed'] = None
        app_key = None

    # 2. Check debug mode
    print(f"\n{Colors.CYAN}[2/5] Checking debug mode...{Colors.END}")
    debug_issues = check_debug_mode(url)
    if debug_issues:
        print(f"  {Colors.RED}✗ VULNERABLE - Debug mode indicators found!{Colors.END}")
        for issue in debug_issues:
            print(f"    - {issue}")
        results['checks']['debug_mode'] = debug_issues
    else:
        print(f"  {Colors.GREEN}✓ OK - No debug mode indicators{Colors.END}")
        results['checks']['debug_mode'] = None

    # 3. Check version disclosure
    print(f"\n{Colors.CYAN}[3/5] Checking version disclosure...{Colors.END}")
    version_info = check_laravel_version(url)
    if version_info:
        print(f"  {Colors.YELLOW}⚠ Version information disclosed:{Colors.END}")
        for k, v in version_info.items():
            print(f"    - {k}: {v}")
        results['checks']['version_disclosure'] = version_info
    else:
        print(f"  {Colors.GREEN}✓ OK - No version disclosure{Colors.END}")
        results['checks']['version_disclosure'] = None

    # 4. Check RCE vulnerability (only if we have APP_KEY)
    print(f"\n{Colors.CYAN}[4/5] Checking RCE vulnerability (CVE-2021-3129)...{Colors.END}")
    if app_key:
        rce_result = check_rce_vulnerable(url, app_key)
        if rce_result.get('vulnerable') == True:
            print(f"  {Colors.RED}✗ POTENTIALLY VULNERABLE to RCE!{Colors.END}")
            print(f"    Indicator: {rce_result.get('indicator')}")
        elif rce_result.get('vulnerable') == 'UNKNOWN':
            print(f"  {Colors.YELLOW}? Could not test: {rce_result.get('reason')}{Colors.END}")
        else:
            print(f"  {Colors.GREEN}✓ OK - No RCE indicators{Colors.END}")
        results['checks']['rce_vulnerable'] = rce_result
    else:
        print(f"  {Colors.YELLOW}? Skipped - No APP_KEY available for testing{Colors.END}")
        results['checks']['rce_vulnerable'] = {'skipped': True, 'reason': 'No APP_KEY'}

    # 5. Check other common issues
    print(f"\n{Colors.CYAN}[5/5] Checking common misconfigurations...{Colors.END}")
    other_issues = check_common_vulnerabilities(url)
    if other_issues:
        print(f"  {Colors.RED}✗ Issues found:{Colors.END}")
        for issue in other_issues:
            print(f"    - {issue['path']}: {issue['issue']}")
        results['checks']['other_issues'] = other_issues
    else:
        print(f"  {Colors.GREEN}✓ OK - No common misconfigurations{Colors.END}")
        results['checks']['other_issues'] = None

    # Summary
    print(f"\n{Colors.BLUE}{'='*60}{Colors.END}")
    vuln_count = sum(1 for k, v in results['checks'].items() if v and v != {'skipped': True, 'reason': 'No APP_KEY'})
    if vuln_count > 0:
        print(f"{Colors.RED}{Colors.BOLD}RESULT: {vuln_count} potential issue(s) found!{Colors.END}")
    else:
        print(f"{Colors.GREEN}{Colors.BOLD}RESULT: No issues found - looking good!{Colors.END}")
    print(f"{Colors.BLUE}{'='*60}{Colors.END}\n")

    return results

def main():
    banner()

    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <url or file>")
        print(f"\nExamples:")
        print(f"  {sys.argv[0]} https://example.com")
        print(f"  {sys.argv[0]} urls.txt")
        sys.exit(1)

    target = sys.argv[1]

    # Check if it's a file with multiple URLs
    if target.endswith('.txt') and not target.startswith('http'):
        try:
            with open(target) as f:
                urls = [line.strip() for line in f if line.strip() and not line.startswith('#')]
            print(f"Loaded {len(urls)} URLs from {target}\n")

            all_results = []
            for url in urls:
                result = scan_url(url)
                all_results.append(result)

            # Save results
            output_file = f"laravel_scan_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            with open(output_file, 'w') as f:
                json.dump(all_results, f, indent=2)
            print(f"\n{Colors.GREEN}Results saved to: {output_file}{Colors.END}")

        except FileNotFoundError:
            print(f"{Colors.RED}File not found: {target}{Colors.END}")
            sys.exit(1)
    else:
        # Single URL
        scan_url(target)

if __name__ == "__main__":
    main()
