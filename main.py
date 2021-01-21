# Created by Bash, Emily Black, yby1973 and 0x74ngly
# Credit to Merubokkusu for recaptcha.


API_KEY = '' # Your 2captcha API KEY

#####################################################
#####################################################
#####################################################
#        AUTHORISED ACCESS FOR MEMBERS ONLY         #
#                  DONT EDIT BELOW                  #
#####################################################
#####################################################
#####################################################






import json
import requests
from requests.structures import CaseInsensitiveDict
import threading # installed on threaded?
import string
import random
from colorama import init
from art import *
from time import sleep
init()

lock = threading.Lock()
success = 0
failed = 0
retries = 0
site_key = '6Lef5iQTAAAAAKeIvIY-DeexoO3gj7ryl9rLMEnn' 

class Fore:
    RESET   = '\033[39m'
    BLACK   = '\033[90m'
    RED     = '\033[91m'
    GREEN   = '\033[92m'
    YELLOW  = '\033[93m'
    BLUE    = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN    = '\033[96m'
    WHITE   = '\033[97m'
    UI1     = '\033[37m'
    UI2     = '\033[90m'

UI = f'''                                              
{Fore.RED} ██╗   ██╗ █████╗ ███╗   ██╗██████╗  █████╗ ███████╗███████╗ ██████╗
{Fore.RED} ██║   ██║██╔══██╗████╗  ██║██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
{Fore.RED} ██║   ██║███████║██╔██╗ ██║██║  ██║███████║███████╗█████╗  ██║     
{Fore.RED} ╚██╗ ██╔╝██╔══██║██║╚██╗██║██║  ██║██╔══██║╚════██║██╔══╝  ██║     
{Fore.RED} ╚████╔╝ ██║  ██║██║ ╚████║██████╔╝██║  ██║███████║███████╗╚██████╗
{Fore.RED}  ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ {Fore.RESET}
'''

print(UI)


# Used by solve() function #
api_url = "https://discord.com/api/v8/auth/register"

def random_string(length):
    return ''.join(random.choice(string.ascii_lowercase + string.digits + '_') for _ in range(length))

def trash_string(length):
    re = ''.join(random.choice(string.ascii_letters + string.digits + '_$\'\\"-?`^~!@#Â¤%&/()Â£${}[]|*-.,;:<>') for _ in range(length))
    return re

def randString(length):
    re = ''.join(random.choice(string.ascii_letters + string.digits + '_$-%^./?*ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789¤()Â£') for _ in range(length))
    return re

def solve():
        s = requests.Session()
        captcha_id = s.post("http://2captcha.com/in.php?key={}&method=userrecaptcha&googlekey={}&pageurl={}".format(API_KEY, site_key, api_url)).text.split('|')[1]
        recaptcha_answer = s.get("http://2captcha.com/res.php?key={}&action=get&id={}".format(API_KEY, captcha_id)).text
        print("solving captcha...")
        while 'CAPCHA_NOT_READY' in recaptcha_answer:
            print(recaptcha_answer)
            sleep(15)
            recaptcha_answer = s.get("http://2captcha.com/res.php?key={}&action=get&id={}".format(API_KEY, captcha_id)).text
        recaptcha_answer = recaptcha_answer.split('|')[1]
        return recaptcha_answer



#threads = 0
def create_account(key='', email=None, username='', cookie=None, fingerprint=None, verbose=True):
    key = solve()
    username = randString(random.randint(3,32))
    global success, failed, retries
    tries = 0
    print(username)
    jsondata = {
        "fingerprint": "",
        "username":"{}".format(username),
        "email":random_string(random.randint(3, 16)) + '@' + random.choice(['gmail.com', 'sol.dk', 'yahoo.com', 'stramkurs.dk', 'venstre.dk', 'facebook.com']),
        "password":"{}".format(trash_string(8)), # Need to be 6 or higher
        "invite":"null",
        "consent":True,
        "date_of_birth":"2006-01-01", # won't succeed logging in if it's under 13
        "gift_card_sku_id":"null",
        "captcha_key":key
    }

    headers = CaseInsensitiveDict()
    headers["authority"] = "discord.com"
    headers["method"] = "POST"
    headers["path"] = "/api/v8/auth/register"
    headers["scheme"] = "https"
    headers["accept"] = "*/*"
    headers["accept-encoding"] = "gzip, deflate, br"
    headers["accept-language"] = "en-US"
    headers["authorization"] = "undefined"
    headers["content-length"] = "249"
    headers["cookie"] = "{}".format(cookie)
    headers["origin"] = "https://discord.com"
    headers["referer"] = "https://discord.com/register"
    headers["sec-fetch-dest"] = "empty"
    headers["sec-fetch-mode"] = "cors"
    headers["sec-fetch-site"] = "same-origin"
    headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"
    headers["x-fingerprint"] = "{}".format(fingerprint)
    headers["x-super-properties"] = "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzg2LjAuNDI0MC4xODMgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6Ijg2LjAuNDI0MC4xODMiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6NzA3ODEsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
    r = requests.post(url="https://discord.com/api/v8/auth/register",headers=headers,json=jsondata)
    if verbose == True:
        if r.status_code == 201:
            f = open("tokens.txt", "a")
            f.write(json.loads(r.content)['token'])
            f.write("\n")
            f.close()
            success += 1
            print(Fore.GREEN + "[{}] Successfully created account".format(r.status_code) + Fore.WHITE)
        else:
            lock.acquire()
            failed += 1
            print(Fore.RED + "Could not create account" + Fore.WHITE)
            print(Fore.YELLOW + "[{}] Response:".format(r.status_code), r.content, Fore.WHITE)
    tries += 1

def main():
    threads = []
    for i in range(300):
        thread = threading.Thread(target=create_account(), daemon=True)
        threads.append(thread)
        thread.start()
        print(f'Account #{i} has been created')
    for thread in threads:
        thread.join()



if __name__ == '__main__':
    main()
