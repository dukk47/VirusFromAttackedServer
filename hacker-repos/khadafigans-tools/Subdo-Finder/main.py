import sys
import os
import time
import requests
from datetime import datetime
from multiprocessing import Pool, Manager
from functools import partial
from pystyle import Write, Colors, Colorate, Center
from colorama import init, Fore, Style

init(autoreset=True)

# === HARDCODE YOUR API ENDPOINT AND KEY HERE ===
API_ENDPOINT = "https://yourdomain.com/api.php" # <- (DM : @marleyybob123 on telegram to get api endpoint)
API_KEY = "SUBDO-BOB-APIKEY123456" # <- Input your apikey here (DM : @marleyybob123 on telegram to get apikey)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_ascii():
    smtp_checker = r"""

███████╗██╗   ██╗██████╗ ██████╗  ██████╗     ███████╗██╗███╗   ██╗██████╗ ███████╗██████╗ 
██╔════╝██║   ██║██╔══██╗██╔══██╗██╔═══██╗    ██╔════╝██║████╗  ██║██╔══██╗██╔════╝██╔══██╗
███████╗██║   ██║██████╔╝██║  ██║██║   ██║    █████╗  ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝
╚════██║██║   ██║██╔══██╗██║  ██║██║   ██║    ██╔══╝  ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
███████║╚██████╔╝██████╔╝██████╔╝╚██████╔╝    ██║     ██║██║ ╚████║██████╔╝███████╗██║  ██║
╚══════╝ ╚═════╝ ╚═════╝ ╚═════╝  ╚═════╝     ╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                                                
   """
    by = r"""
                                 
                        ██████╗ ██╗   ██╗
                        ██╔══██╗╚██╗ ██╔╝
                        ██████╔╝ ╚████╔╝ 
                        ██╔══██╗  ╚██╔╝  
                        ██████╔╝   ██║   
                        ╚═════╝    ╚═╝   
                 
    """
    bob_marley = r"""

██████╗  ██████╗ ██████╗     ███╗   ███╗ █████╗ ██████╗ ██╗     ███████╗██╗   ██╗
██╔══██╗██╔═══██╗██╔══██╗    ████╗ ████║██╔══██╗██╔══██╗██║     ██╔════╝╚██╗ ██╔╝
██████╔╝██║   ██║██████╔╝    ██╔████╔██║███████║██████╔╝██║     █████╗   ╚████╔╝ 
██╔══██╗██║   ██║██╔══██╗    ██║╚██╔╝██║██╔══██║██╔══██╗██║     ██╔══╝    ╚██╔╝  
██████╔╝╚██████╔╝██████╔╝    ██║ ╚═╝ ██║██║  ██║██║  ██║███████╗███████╗   ██║   
╚═════╝  ╚═════╝ ╚═════╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝   ╚═╝   
                                                                                 
   """
    print()
    print(Center.XCenter(Colorate.Horizontal(Colors.red_to_green, smtp_checker, 1)))
    print(Center.XCenter(Colorate.Horizontal(Colors.yellow_to_green, by, 1)))
    print(Center.XCenter(Colorate.Horizontal(Colors.red_to_green, bob_marley, 1)))
    print()

def save_subdomains(subdomains, lock, output_file):
    if not subdomains:
        return
    with lock:
        with open(output_file, "a") as f:
            for sub in subdomains:
                f.write(sub + "\n")

def fetch_domain(domain, lock, output_file):
    print(f"{Fore.BLUE}🔵 {domain}{Style.RESET_ALL}")
    try:
        params = {'domain': domain, 'key': API_KEY}
        resp = requests.get(API_ENDPOINT, params=params, timeout=60)
        data = resp.json()
        if 'error' in data:
            print(f"  {Fore.RED}[!] {data['error']}{Style.RESET_ALL}")
            return
        subdomains = data.get('subdomains', [])
        if subdomains:
            save_subdomains(subdomains, lock, output_file)
            for sub in subdomains:
                print(f"  {Fore.GREEN}[+] {sub}{Style.RESET_ALL}")
        else:
            print(f"  {Fore.YELLOW}[!] No subdomains found.{Style.RESET_ALL}")
            save_subdomains([domain], lock, output_file)
    except Exception as e:
        print(f"  {Fore.RED}[!] Error scanning {domain}: {e}{Style.RESET_ALL}")
    print()

def read_domains(file_path):
    try:
        with open(file_path, 'r') as file:
            domains = [line.strip() for line in file if line.strip()]
        return domains
    except FileNotFoundError:
        print(f"{Fore.RED}Error: File {file_path} not found.{Style.RESET_ALL}")
        sys.exit(1)
    except Exception as e:
        print(f"{Fore.RED}Error reading file: {e}{Style.RESET_ALL}")
        sys.exit(1)

def main():
    clear()
    print_ascii()
    file_path = Write.Input("Enter the path to your domain list file (e.g., domains.txt): ", Colors.green_to_yellow, interval=0.005)
    if not file_path:
        Write.Print("Error: No file path provided.\n", Colors.red_to_yellow, interval=0.002)
        sys.exit(1)
    try:
        thread_count = int(Write.Input("Thread count: ", Colors.green_to_yellow, interval=0.005))
    except Exception:
        thread_count = 5

    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"Scan-result/result_{current_time}.txt"
    os.makedirs("Scan-result", exist_ok=True)
    Write.Print(f"Results will be saved to {output_file}\n", Colors.green_to_yellow, interval=0.005)
    Write.Print("Starting subdomain scan...\n", Colors.green_to_yellow, interval=0.005)
    domains = read_domains(file_path)
    total_domains = len(domains)
    Write.Print(f"Total domains to scan: {total_domains}\n\n", Colors.green_to_yellow, interval=0.005)
    Write.Print("Scan Results:\n", Colors.green_to_yellow, interval=0.001)
    Write.Print("="*60 + "\n", Colors.green_to_yellow, interval=0.001)
    open(output_file, 'w').close()
    with Manager() as manager:
        lock = manager.Lock()
        with Pool(processes=thread_count) as pool:
            pool.map(partial(fetch_domain, lock=lock, output_file=output_file), domains)
    try:
        with open(output_file, 'r') as f:
            all_subdomains = [line.strip() for line in f if line.strip()]
    except Exception:
        all_subdomains = []
    Write.Print(f"\nScan complete. Processed {total_domains} domains.\n", Colors.green_to_yellow, interval=0.005)
    Write.Print(f"Total results saved: {len(all_subdomains)}\n", Colors.green_to_yellow, interval=0.005)
    Write.Print(f"All results have been saved to {output_file}\n", Colors.green_to_yellow, interval=0.005)

if __name__ == "__main__":
    main()
