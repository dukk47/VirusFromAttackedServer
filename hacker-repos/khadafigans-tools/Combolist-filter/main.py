import os
from pystyle import Colorate, Colors, Center, Write
from datetime import datetime

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_ascii():
    smtp_checker = r"""

 ██████╗ ██████╗ ███╗   ███╗██████╗  ██████╗ ██╗     ██╗███████╗████████╗    ███████╗██╗██╗  ████████╗███████╗██████╗ 
██╔════╝██╔═══██╗████╗ ████║██╔══██╗██╔═══██╗██║     ██║██╔════╝╚══██╔══╝    ██╔════╝██║██║  ╚══██╔══╝██╔════╝██╔══██╗
██║     ██║   ██║██╔████╔██║██████╔╝██║   ██║██║     ██║███████╗   ██║       █████╗  ██║██║     ██║   █████╗  ██████╔╝
██║     ██║   ██║██║╚██╔╝██║██╔══██╗██║   ██║██║     ██║╚════██║   ██║       ██╔══╝  ██║██║     ██║   ██╔══╝  ██╔══██╗
╚██████╗╚██████╔╝██║ ╚═╝ ██║██████╔╝╚██████╔╝███████╗██║███████║   ██║       ██║     ██║███████╗██║   ███████╗██║  ██║
 ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝  ╚═════╝ ╚══════╝╚═╝╚══════╝   ╚═╝       ╚═╝     ╚═╝╚══════╝╚═╝   ╚══════╝╚═╝  ╚═╝
                                                                                                
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

def main():
    clear()
    print_ascii()
    # Prompt for input file
    input_file = Write.Input("Give me your List:", Colors.green_to_yellow, interval=0.005)
    if not os.path.isfile(input_file):
        print(Colorate.Horizontal(Colors.red_to_yellow, f"[!] File '{input_file}' not found."))
        return

    # Output file with timestamp
    out_name = f"filtered_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    domains = ["hotmail.com", "outlook.com", "msn.com", "live.com"] # Edit domain here
    count = 0

    with open(input_file, 'r', encoding='utf-8', errors='ignore') as infile, \
         open(out_name, 'w', encoding='utf-8') as outfile:
        for line in infile:
            line = line.strip()
            if '|' in line:
                email, password = line.split('|', 1)
                domain = email.split('@')[-1].lower()
                if domain in domains:
                    print(Colorate.Horizontal(Colors.cyan_to_green, f"[+] {email}|{password}"))
                    outfile.write(f"{email}|{password}\n")
                    count += 1

    print(Colorate.Horizontal(Colors.yellow_to_green, f"\n[+] Total filtered combos: {count}"))
    print(Colorate.Horizontal(Colors.green_to_yellow, f"[+] Saved to: {out_name}\n"))

if __name__ == "__main__":
    main()
