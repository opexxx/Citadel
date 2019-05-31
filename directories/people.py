# -*- coding: utf-8 -*-
from colorama import init
from colorama import Fore
import webbrowser
import time
from . import menu
import subprocess

def people():
    time.sleep(0.5)
    toolSelect = input(Fore.YELLOW + " Select: " + Fore.WHITE)
    print()
    if toolSelect == "1":
        print(Fore.RED + " SkipTracer - scrape PII paywall sites on a ramen noodle budget")
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
            webbrowser.open('https://github.com/xillwillx/skiptracer')
        elif view_or_download == "2":
            print(Fore.CYAN + " [+] " + Fore.WHITE + "Downloading SkipTracer")
            time.sleep(0.5)
            print()
            subprocess.call(['git', 'clone', 'https://github.com/xillwillx/skiptracer.git'])
        elif view_or_download == "<":
            menu.menu()
    elif toolSelect == "2":
        print(Fore.RED + " LittleBrother - information gathering tool for EU persons")
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
            webbrowser.open('https://github.com/lulz3xploit/LittleBrother')
        elif view_or_download == "2":
            print(Fore.CYAN + " [+] " + Fore.WHITE + "Downloading LittleBrother")
            time.sleep(0.5)
            print()
            subprocess.call(['git', 'clone', 'https://github.com/lulz3xploit/LittleBrother.git'])
        elif view_or_download == "<":
            menu.menu()
    elif toolSelect == "3":
        print(Fore.RED + " SocialScan - check email addresses across all social platforms")
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
            webbrowser.open('https://github.com/iojw/socialscan')
        elif view_or_download == "2":
            print(Fore.CYAN + " [+] " + Fore.WHITE + "Downloading SocialScan")
            time.sleep(0.5)
            print()
            subprocess.call(['git', 'clone', 'https://github.com/iojw/socialscan.git'])
        elif view_or_download == "<":
            menu.menu()
    elif toolSelect == "4":
        print(Fore.RED + " Sherlock - search username availability across all social platforms")
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
            webbrowser.open('https://github.com/sherlock-project/sherlock')
        elif view_or_download == "2":
            print(Fore.CYAN + " [+] " + Fore.WHITE + "Downloading Sherlock")
            time.sleep(0.5)
            print()
            subprocess.call(['git', 'clone', 'https://github.com/sherlock-project/sherlock.git'])
        elif view_or_download == "<":
            menu.menu()
    elif toolSelect == "<":
        menu.menu()
    people()

#test
