import random
import string
import webbrowser
import requests
import json
import gratient
import pygetwindow as gw
import os
import time

os.system("cls" if os.name == "nt" else "clear")
window = gw.getActiveWindow()
window.resizeTo(600, 1000)
window.activate()

def print_banner():
    banner = (gratient.purple("""
    ____                  __                _                
   / __ \____ _____  ____/ /___  ____ ___  (_)___  ___  _____
  / /_/ / __ `/ __ \/ __  / __ \/ __ `__ \/ /_  / / _ \/ ___/
 / _, _/ /_/ / / / / /_/ / /_/ / / / / / / / / /_/  __/ /    
/_/ |_|\__,_/_/ /_/\__,_/\____/_/ /_/ /_/_/ /___/\___/_/
                                                              
                    Trying2bAHacker 
                              
                              """))
    print(banner)

def open_or_close(url, open_in_browser):
    response = requests.head(url)
    
    if response.status_code == 404:
        print(gratient.purple(f"The page {url} does not exist (404)."))
        return False
    else:
        print(gratient.green(f"The page {url} exists."))
        if open_in_browser:
            webbrowser.open(url)
            print(gratient.green("Opening in the web browser..."))
        return True

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print_banner()

    print(gratient.purple("Choose a domain:"))
    print(gratient.purple("[*] 1. paster.so (currenty doesn't work)"))
    print(gratient.purple(f"[*] 2. rentry.co"))
    
    choice = input(gratient.purple(f"[>] Enter the number of the domain: "))

    #if choice == '1':

        #domain = "paster.so"
        #combinations = 4
        #letters = string.ascii_letters
    if choice == '2':
        domain = "rentry.co"
        combinations = 5
        letters = string.ascii_lowercase
    else:
        print(gratient.red("[X] Invalid choice. Please enter 1 (does'nt work or 2."))
        time.sleep(4)
        continue

    number_of_attempts = int(input(gratient.purple("[>] Stop when amount is hit: ")))

    if number_of_attempts < 0:
        print(gratient.red("[X] The number of attempts must be above 0. Try again."))
        time.sleep(4)
        continue

    open_in_browser = input(gratient.purple("[>] Auto open URL's? (y/n): ")).lower() == 'y'

    successful_urls = []

    while (number_of_attempts == 0 and not successful_urls) or (number_of_attempts > 0 and len(successful_urls) < number_of_attempts):
        link = "https://" + domain + "/"
        random_end = ''.join(random.choice(letters + string.digits) for _ in range(combinations))
        url = link + random_end

        if open_or_close(url, open_in_browser):
            successful_urls.append(url)
            status = "[✓] "
            print(gratient.green(status + url))
        else:
            status = "[X] "
            print(gratient.blue(status + url))

    existing_urls = []
    if os.path.exists('success_urls.json'):
        with open('success_urls.json', 'r') as json_file:
            existing_urls = json.load(json_file)

    existing_urls.extend(successful_urls)

    with open('success_urls.json', 'w') as json_file:
        json.dump(existing_urls, json_file, indent=2)

    print(gratient.purple("Successful URLs have been saved in success_urls.json."))

    try_again = input(gratient.purple("[>] Do you want to try again? (yes/no): "))
    if try_again.lower() != 'yes':
        break
    os.system("cls" if os.name == "nt" else "clear")
