# -*- coding: utf-8 -*-
from colorama import init
from colorama import Fore
import webbrowser
import time
from . import menu
import subprocess

def recon():
    time.sleep(0.5)
    toolSelect = input(Fore.YELLOW + " Select: " + Fore.WHITE)
    print()
    if toolSelect == "1":
        print(Fore.RED + " Photon - an incredibly fast crawler designed for OSINT")
        print()
        options = [
        Fore.CYAN + " [1]" + Fore.WHITE + " View the tool",
        Fore.CYAN + " [2]" + Fore.WHITE + " Download the tool",
        Fore.CYAN + " [<]" + Fore.WHITE + " Main menu"
        ]
        print(*options,sep='\n')
        print()
        time.sleep(0.75)
        view_or_download = input(Fore.YELLOW + " Select: " + Fore.WHITE)
        print()
        if view_or_download == "1":
            webbrowser.open('https://github.com/s0md3v/Photon')
        elif view_or_download == "2":
            print(Fore.CYAN + " [+] " + Fore.WHITE + "Downloading Photon")
            time.sleep(0.5)
            print()
            subprocess.call(['git', 'clone', 'https://github.com/s0md3v/Photon.git'])
        elif view_or_download == "<":
            menu.menu()

    elif toolSelect == "2":
        print(Fore.RED + " GasMask - an all in one OSINT gathering tool")
        print()
        options = [
        Fore.CYAN + " [1]" + Fore.WHITE + " View the tool",
        Fore.CYAN + " [2]" + Fore.WHITE + " Download the tool",
        Fore.CYAN + " [<]" + Fore.WHITE + " Main menu"
        ]
        print(*options,sep='\n')
        print()
        time.sleep(0.5)
        view_or_download = input(Fore.YELLOW + " Select: " + Fore.WHITE)
        print()
        if view_or_download == "1":
            webbrowser.open('https://github.com/twelvesec/gasmask')
        elif view_or_download == "2":
            print(Fore.CYAN + " [+] " + Fore.WHITE + "Downloading GasMask")
            time.sleep(0.5)
            print()
            subprocess.call(['git', 'clone', 'https://github.com/twelvesec/gasmask.git'])
        elif view_or_download == "<":
            menu.menu()

    elif toolSelect == "3":
        print(Fore.RED + " Kamerka - build an interactive map of cameras from Shodan")
        print()
        options = [
        Fore.CYAN + " [1]" + Fore.WHITE + " View the tool",
        Fore.CYAN + " [2]" + Fore.WHITE + " Download the tool",
        Fore.CYAN + " [<]" + Fore.WHITE + " Main menu"
        ]
        print(*options,sep='\n')
        print()
        time.sleep(0.5)
        view_or_download = input(Fore.YELLOW + " Select: " + Fore.WHITE)
        print()
        if view_or_download == "1":
            webbrowser.open('https://github.com/woj-ciech/kamerka')
        elif view_or_download == "2":
            print(Fore.CYAN + " [+] " + Fore.WHITE + "Downloading Kamerka")
            time.sleep(0.5)
            print()
            subprocess.call(['git', 'clone', 'https://github.com/woj-ciech/kamerka.git'])
        elif view_or_download == "<":
            menu.menu()

    elif toolSelect == "4":
        print(Fore.RED + " FinalRecon - an OSINT tool for all in one web reconnaissance")
        print()
        options = [
        Fore.CYAN + " [1]" + Fore.WHITE + " View the tool",
        Fore.CYAN + " [2]" + Fore.WHITE + " Download the tool",
        Fore.CYAN + " [<]" + Fore.WHITE + " Main menu"
        ]
        print(*options,sep='\n')
        print()
        time.sleep(0.5)
        view_or_download = input(Fore.YELLOW + " Select: " + Fore.WHITE)
        print()
        if view_or_download == "1":
            webbrowser.open('https://github.com/thewhiteh4t/FinalRecon')
        elif view_or_download == "2":
            print(Fore.CYAN + " [+] " + Fore.WHITE + "Downloading Kamerka")
            time.sleep(0.5)
            print()
            subprocess.call(['git', 'clone', 'https://github.com/thewhiteh4t/FinalRecon.git'])
        elif view_or_download == "<":
            menu.menu()

    elif toolSelect == "5":
        print(Fore.RED + " SpiderFoot - automate OSINT from hundreds of sources")
        print()
        options = [
        Fore.CYAN + " [1]" + Fore.WHITE + " View the tool",
        Fore.CYAN + " [2]" + Fore.WHITE + " Download the tool",
        Fore.CYAN + " [<]" + Fore.WHITE + " Main menu"
        ]
        print(*options,sep='\n')
        print()
        time.sleep(0.5)
        view_or_download = input(Fore.YELLOW + " Select: " + Fore.WHITE)
        print()
        if view_or_download == "1":
            webbrowser.open('https://github.com/smicallef/spiderfoot')
        elif view_or_download == "2":
            print(Fore.CYAN + " [+] " + Fore.WHITE + "Downloading Spiderfoot")
            time.sleep(0.5)
            print()
            subprocess.call(['git', 'clone', 'https://github.com/smicallef/spiderfoot.git'])
        elif view_or_download == "<":
            menu.menu()

    elif toolSelect == "6":
        print(Fore.RED + " POCKINT - a portable OSINT Swiss Army Knife for DFIR professionals")
        print()
        options = [
        Fore.CYAN + " [1]" + Fore.WHITE + " View the tool",
        Fore.CYAN + " [2]" + Fore.WHITE + " Download the tool",
        Fore.CYAN + " [<]" + Fore.WHITE + " Main menu"
        ]
        print(*options,sep='\n')
        print()
        time.sleep(0.5)
        view_or_download = input(Fore.YELLOW + " Select: " + Fore.WHITE)
        print()
        if view_or_download == "1":
            webbrowser.open('https://github.com/netevert/pockint')
        elif view_or_download == "2":
            print(Fore.CYAN + " [+] " + Fore.WHITE + "Downloading POCKINT")
            time.sleep(0.5)
            print()
            subprocess.call(['git', 'clone', 'https://github.com/netevert/pockint.git'])
        elif view_or_download == "<":
            menu.menu()

    elif toolSelect == "7":
        print(Fore.RED + " ODIN - automated network asset, email, and social media profile discovery and cataloging")
        print()
        options = [
        Fore.CYAN + " [1]" + Fore.WHITE + " View the tool",
        Fore.CYAN + " [2]" + Fore.WHITE + " Download the tool",
        Fore.CYAN + " [<]" + Fore.WHITE + " Main menu"
        ]
        print(*options,sep='\n')
        print()
        time.sleep(0.5)
        view_or_download = input(Fore.YELLOW + " Select: " + Fore.WHITE)
        print()
        if view_or_download == "1":
            webbrowser.open('https://github.com/chrismaddalena/ODIN')
        elif view_or_download == "2":
            print(Fore.CYAN + " [+] " + Fore.WHITE + "Downloading POCKINT")
            time.sleep(0.5)
            print()
            subprocess.call(['git', 'clone', 'https://github.com/chrismaddalena/ODIN.git'])
        elif view_or_download == "<":
            menu.menu()

    elif toolSelect == "<":
        menu.menu()
    recon()
