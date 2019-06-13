# -*- coding: utf-8 -*-
from colorama import init
from colorama import Fore
import webbrowser
import time
from . import menu
import subprocess

# Dark web tools
def dark():
    time.sleep(0.5)
    toolSelect = input(Fore.YELLOW + " Select: " + Fore.WHITE)
    print()
    if toolSelect == "1":
        print(Fore.RED + " TorBot - a dark web OSINT tool")
        print()
        options = [
        Fore.CYAN + " [1]" + Fore.WHITE + " View the tool",
        Fore.CYAN + " [2]" + Fore.WHITE + " Download the tool",
        Fore.CYAN + " [<]" + Fore.WHITE + " Main menu"
        ]
        print(*options,sep='\n')
        print()
        view_or_download = input(Fore.YELLOW + " Select: " + Fore.WHITE)
        print()
        if view_or_download == "1":
            webbrowser.open('https://github.com/DedSecInside/TorBot')
        elif view_or_download == "2":
            print(Fore.CYAN + " [+] " + Fore.WHITE + "Downloading TorBot")
            time.sleep(0.5)
            print()
            subprocess.call(['git', 'clone', 'https://github.com/DedSecInside/TorBot.git'])
        elif view_or_download == "<":
            menu.menu()

    elif toolSelect == "2":
        print(Fore.RED + " Onioff - an onion url inspector for inspecting deep web links")
        print()
        options = [
        Fore.CYAN + " [1]" + Fore.WHITE + " View the tool",
        Fore.CYAN + " [2]" + Fore.WHITE + " Download the tool",
        Fore.CYAN + " [<]" + Fore.WHITE + " Main menu",
        ]
        print(*options,sep='\n')
        print()
        view_or_download = input(Fore.YELLOW + " Select: " + Fore.WHITE)
        print()
        if view_or_download == "1":
            webbrowser.open('https://github.com/k4m4/onioff')
        elif view_or_download == "2":
            print(Fore.CYAN + " [+] " + Fore.WHITE +  "Downloading Onioff")
            time.sleep(0.5)
            print()
            subprocess.call(['git', 'clone', 'https://github.com/k4m4/onioff.git'])
        elif view_or_download == "<":
            menu.menu()

    elif toolSelect == "3":
        print(Fore.RED + " Fresh Onions - an open source tor spider/onion crawler")
        print()
        options = [
        Fore.CYAN + " [1]" + Fore.WHITE + " View the tool",
        Fore.CYAN + " [2]" + Fore.WHITE + " Download the tool",
        Fore.CYAN + " [<]" + Fore.WHITE + " Main menu",
        ]
        print(*options,sep='\n')
        print()
        view_or_download = input(Fore.YELLOW + " Select: " + Fore.WHITE)
        print()
        if view_or_download == "1":
            webbrowser.open('https://github.com/dirtyfilthy/freshonions-torscraper')
        elif view_or_download == "2":
            print(Fore.CYAN + " [+] " + Fore.WHITE +  "Downloading Fresh Onions")
            time.sleep(0.5)
            print()
            subprocess.call(['git', 'clone', 'https://github.com/dirtyfilthy/freshonions-torscraper.git'])
        elif view_or_download == "<":
            menu.menu()

    elif toolSelect == "4":
        print(Fore.RED + " Dark Scrape - an OSINT tool to find media links in tor sites")
        print()
        options = [
        Fore.CYAN + " [1]" + Fore.WHITE + " View the tool",
        Fore.CYAN + " [2]" + Fore.WHITE + " Download the tool",
        Fore.CYAN + " [<]" + Fore.WHITE + " Main menu",
        ]
        print(*options,sep='\n')
        print()
        view_or_download = input(Fore.YELLOW + " Select: " + Fore.WHITE)
        print()
        if view_or_download == "1":
            webbrowser.open('https://github.com/itsmehacker/DarkScrape')
        elif view_or_download == "2":
            print(Fore.CYAN + " [+] " + Fore.WHITE +  "Downloading Dark Scrape")
            time.sleep(0.5)
            print()
            subprocess.call(['git', 'clone', 'https://github.com/itsmehacker/DarkScrape.git'])
        elif view_or_download == "<":
            menu.menu()

    elif toolSelect == "5":
        print(Fore.RED + " Darklight - collects onion domains and crawls webpages")
        print()
        options = [
        Fore.CYAN + " [1]" + Fore.WHITE + " View the tool",
        Fore.CYAN + " [2]" + Fore.WHITE + " Download the tool",
        Fore.CYAN + " [<]" + Fore.WHITE + " Main menu",
        ]
        print(*options,sep='\n')
        print()
        view_or_download = input(Fore.YELLOW + " Select: " + Fore.WHITE)
        print()
        if view_or_download == "1":
            webbrowser.open('https://github.com/bunseokbot/darklight')
        elif view_or_download == "2":
            print(Fore.CYAN + " [+] " + Fore.WHITE +  "Downloading Dark Scrape")
            time.sleep(0.5)
            print()
            subprocess.call(['git', 'clone', 'https://github.com/bunseokbot/darklight.git'])
        elif view_or_download == "<":
            menu.menu()
    elif toolSelect == "<":
        menu.menu()
    dark()
