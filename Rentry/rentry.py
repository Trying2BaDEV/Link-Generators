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
# Find the active window
window = gw.getActiveWindow()

# Resize the window
window.resizeTo(600, 1000)  # You can adjust the desired width and height

# Stay active until the window is closed
window.activate()

def print_banner():
    banner = (gratient.purple("""    ____             __                                      
   / __ \___  ____  / /________  __                          
  / /_/ / _ \/ __ \/ __/ ___/ / / /                          
 / _, _/  __/ / / / /_/ /  / /_/ /                           
/_/ |_|\___/_/ /_/\__/_/   \__, /                            
    ____                  /____/            _                
   / __ \____ _____  ____/ /___  ____ ___  (_)___  ___  _____
  / /_/ / __ `/ __ \/ __  / __ \/ __ `__ \/ /_  / / _ \/ ___/
 / _, _/ /_/ / / / / /_/ / /_/ / / / / / / / / /_/  __/ /    
/_/ |_|\__,_/_/ /_/\__,_/\____/_/ /_/ /_/_/ /___/\___/_/     
                                                              
                    Trying2bAHacker 
                              
                              """))
    print(banner)

def open_or_close(url):
    response = requests.head(url)
    
    if response.status_code == 404:
        print(gratient.purple(f"The page {url} does not exist (404)."))
        return False
    else:
        print(gratient.green(f"The page {url} exists. Opening..."))
        webbrowser.open(url)
        return True

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print_banner()
    number_of_attempts = int(input(gratient.purple("[>] Enter the number of attempts (0 = until 1 valid): ")))

    if number_of_attempts < 0:
        print(gratient.red("[X] The number of attempts must be above 0. Try again."))
        time.sleep(4)
        continue

    successful_urls = []

    while (number_of_attempts == 0 and not successful_urls) or (number_of_attempts > 0 and len(successful_urls) < number_of_attempts):
        link = "https://rentry.co/"
        random_end = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))
        url = link + random_end

        if open_or_close(url):
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
