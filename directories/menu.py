# -*- coding: utf-8 -*-
from colorama import init
from colorama import Fore
import webbrowser
import time
import subprocess
from .recon import *
from .people import *
from .social import *
from .paste import *
from .dark import *


init(autoreset=True)

def menu():
    print()
    print("""  ██████╗██╗████████╗ █████╗ ██████╗ ███████╗██╗
 ██╔════╝██║╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║
 ██║     ██║   ██║   ███████║██║  ██║█████╗  ██║
 ██║     ██║   ██║   ██╔══██║██║  ██║██╔══╝  ██║
 ╚██████╗██║   ██║   ██║  ██║██████╔╝███████╗███████╗
  ╚═════╝╚═╝   ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝    """)
    print(" A library of OSINT tools")
    print()
    print(Fore.CYAN + " [1]" + Fore.WHITE + " Recon tools")
    print(Fore.CYAN + " [2]" + Fore.WHITE + " People search tools")
    print(Fore.CYAN + " [3]" + Fore.WHITE + " Social media tools")
    print(Fore.CYAN + " [4]" + Fore.WHITE + " Paste site tools")
    print(Fore.CYAN + " [5]" + Fore.WHITE + " Dark web tools")
    print()
    print(Fore.RED + " [+]" + Fore.WHITE + " Update The Citadel")
    print()
    print(Fore.YELLOW + " New tools available in the Citadel: Fresh Onions, Dark Scrape, Darklight")
    print()
    print(Fore.RED + " [x]" + Fore.WHITE + " Exit")
    print()
    directory = input(" Select a directory: ")
    print()
    if directory == "1":
        print(Fore.YELLOW + " Recon tools" + Fore.WHITE + " - all in one OSINT tools that serve multiple functions")
        print()
        tools = [
        Fore.CYAN + " [1]" + Fore.WHITE + " Photon - an incredibly fast crawler designed for OSINT",
        Fore.CYAN + " [2]" + Fore.WHITE + " GasMask - an all in one OSINT gathering tool",
        Fore.CYAN + " [3]" + Fore.WHITE + " Kamerka - build an interactive map of cameras from Shodan",
        Fore.CYAN + " [4]" + Fore.WHITE + " FinalRecon - an OSINT tool for all in one web reconnaissance",
        Fore.CYAN + " [5]" + Fore.WHITE + " SpiderFoot - automate OSINT from hundreds of sources",
        Fore.CYAN + " [6]" + Fore.WHITE + " POCKINT - a portable OSINT Swiss Army Knife for DFIR professionals",
        Fore.CYAN + " [7]" + Fore.WHITE + " ODIN - network asset, email, and social media discovery and cataloging",
        Fore.CYAN + " [8]" + Fore.WHITE + " h8mail - find passwords through breach and recon services",
        Fore.CYAN + " [9]" + Fore.WHITE + " buster - dig deeper into emails and find linked accounts",
        Fore.CYAN + " [10]" + Fore.WHITE + " PaGoDo - automate Google Dorks",
        Fore.RED + " [<]" + Fore.WHITE + " Main menu"
        ]

        print(*tools, sep='\n')
        print()
        recon()

    elif directory == "2":
        print(Fore.YELLOW + " People search tools" + Fore.WHITE + " - extract OSINT from multiple databases")
        print()
        tools = [
        Fore.CYAN + " [1]" + Fore.WHITE + " Skiptracer - scrape PII paywall sites on a ramen noodle budget",
        Fore.CYAN + " [2]" + Fore.WHITE + " LittleBrother - information gathering tool for EU persons",
        Fore.CYAN + " [3]" + Fore.WHITE + " SocialScan - check email addresses across all social platforms",
        Fore.CYAN + " [4]" + Fore.WHITE + " Sherlock - search username availability across all social platforms",
        Fore.RED + " [<]" + Fore.WHITE + " Main menu"
        ]
        print(*tools, sep='\n')
        print()
        people()

    elif directory == "3":
        socialMenu()
        social()

    elif directory == "4":
        print(Fore.YELLOW + " Paste site tools" + Fore.WHITE + " - collect OSINT from multiple paste sites")
        print()
        tools = [
        Fore.CYAN + " [1]" + Fore.WHITE + " Scavenger - a crawler bot for credential leaks",
        Fore.CYAN + " [2]" + Fore.WHITE + " CardPwn - OSINT Tool to find breached credit card information",
        Fore.RED + " [<]" + Fore.WHITE + " Main menu",
        ]
        print(*tools,sep='\n')
        print()
        paste()

    elif directory == "5":
        print(Fore.YELLOW + " Dark web tools" + Fore.WHITE + " - collect OSINT from dark web sources")
        print()
        tools = [
        Fore.CYAN + " [1]" + Fore.WHITE + " TorBot - dark web OSINT tool",
        Fore.CYAN + " [2]" + Fore.WHITE + " Onioff - an onion url inspector for inspecting deep web links",
        Fore.CYAN + " [3]" + Fore.WHITE + " Fresh Onions - an open source tor spider/onion crawler",
        Fore.CYAN + " [4]" + Fore.WHITE + " Dark Scrape - an OSINT tool to find media links in tor sites",
        Fore.CYAN + " [5]" + Fore.WHITE + " Darklight - collects onion domains and crawls webpages",
        Fore.RED + " [<]" + Fore.WHITE + " Main menu"
        ]
        print(*tools, sep='\n')
        print()
        dark()

    elif directory == "x":
        exit()

    elif directory == "+":
        subprocess.call(["git", "pull"])
        time.sleep(0.5)
        print(Fore.YELLOW + "The Citadel is Updated")
menu()
