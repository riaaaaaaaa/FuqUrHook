# Created by ria | https://github.com/riaaaaaaaa
# Don't be a skid and give some credit if used kthx
# Thats about it ily have fun <3

class INIT:
	__version__ = 1.0

import json,requests,os,time,random,ctypes
from colorama import Fore
req = requests.Session()

with open("config.json", encoding='utf-8', errors='ignore') as f:
	configdata = json.load(f, strict=False)
config = configdata["BotConfig"]
proxies = open('proxies.txt','r').read().splitlines()
proxies = [{'https':'http://'+proxy} for proxy in proxies]

def Menu(): 
	ctypes.windll.kernel32.SetConsoleTitleW(f'[FuqUrHook v{INIT.__version__}] | By ria')
	print(f'''{Fore.RESET}
		  █████▒█    ██   █████   █    ██  ██▀███   ██░ ██  ▒█████   ▒█████   ██ ▄█▀
		▓██   ▒ ██  ▓██▒▒██▓  ██▒ ██  ▓██▒▓██ ▒ ██▒▓██░ ██▒▒██▒  ██▒▒██▒  ██▒ ██▄█▒ 
		▒████ ░▓██  ▒██░▒██▒  ██░▓██  ▒██░▓██ ░▄█ ▒▒██▀▀██░▒██░  ██▒▒██░  ██▒▓███▄░ 
		░▓█▒  ░▓▓█  ░██░░██  █▀ ░▓▓█  ░██░▒██▀▀█▄  ░▓█ ░██ ▒██   ██░▒██   ██░▓██ █▄ 
		░▒█░   ▒▒█████▓ ░▒███▒█▄ ▒▒█████▓ ░██▓ ▒██▒░▓█▒░██▓░ ████▓▒░░ ████▓▒░▒██▒ █▄
		 ▒ ░   ░▒▓▒ ▒ ▒ ░░ ▒▒░ ▒ ░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░ ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒ ▒▒ ▓▒
		 ░     ░░▒░ ░ ░  ░ ▒░  ░ ░░▒░ ░ ░   ░▒ ░ ▒░ ▒ ░▒░ ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░▒ ▒░
		 ░ ░    ░░░ ░ ░    ░   ░  ░░░ ░ ░   ░░   ░  ░  ░░ ░░ ░ ░ ▒  ░ ░ ░ ▒  ░ ░░ ░ 
			  ░         ░       ░        ░      ░  ░  ░    ░ ░      ░ ░  ░  ░   


				{Fore.CYAN}FuqUrHook {INIT.__version__} {Fore.RESET}| {Fore.RED}Type "help" for a list of commands
				{Fore.CYAN}Created by {Fore.RED}ria
				{Fore.CYAN}https://github.com/{Fore.RED}riaaaaaaaa

''' + Fore.RESET)

def Help():
	print(f'''{Fore.RESET}{Fore.RED}		-- Commands are seperated by commas --{Fore.RESET}
{Fore.GREEN}spam,(webhook),(message),(amount) | {Fore.RESET}Spam a given webhook any amount of times
{Fore.GREEN}delete,(webhook) | {Fore.RESET}Forcefully deletes the given webhook, regardless of perms
{Fore.GREEN}getinfo,(webhook) | {Fore.RESET}Gives a list of information about the desired webhook.
{Fore.GREEN}destroy,(webhook) | {Fore.RESET}Completely destroys the given webhook.
{Fore.GREEN}scrape-proxies | {Fore.RESET}Scrapes HTTP proxies from proxyscrape.com and writes them to proxies.txt
{Fore.GREEN}clear | {Fore.RESET}Resets the console
''' + Fore.RESET)
	Start()

def Scrape():
	print(f"[{Fore.GREEN}+{Fore.RESET}] Scraping proxies...")
	try:
		r = req.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1500')
		prox = open("proxies.txt", "a+")
		prox.seek(0)
		prox.truncate()
		proxies = []
		for proxy in r.text.split('\n'):
			proxy = proxy.strip()
			if proxy:
				proxies.append(proxy)
		for p in proxies:
			prox.write((p)+"\n")
		print(f"[{Fore.GREEN}+{Fore.RESET}] Finished!")
	except Exception as e:
		print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
	Start()

def Spam(webhook, message, amount):
	try:
		print(config["useproxy"])
		if config["useproxy"] == True:
			proxy = proxy = random.choice(proxies)
			for _ in range(amount):
				r = req.post(webhook, json = {'content':f'{message}','username':config["username"],'avatar_url':config["avatar"]}, proxies = proxy)
				if r.status_code == 204:
					print(f"[{Fore.GREEN}+{Fore.RESET}] Sent message!")
				elif r.status_code == 404:
					print(f"[{Fore.YELLOW}-{Fore.RESET}] Invalid webhook")
				else:
					print(f"[{Fore.YELLOW}-{Fore.RESET}] Unknown Error")
		else:
			for _ in range(amount):
				r = req.post(webhook, json = {'content':f'{message}','username':config["username"],'avatar_url':config["avatar"]})
				if r.status_code == 204:
					print(f"[{Fore.GREEN}+{Fore.RESET}] Sent message!")
				elif r.status_code == 404:
					print(f"[{Fore.YELLOW}-{Fore.RESET}] Invalid webhook")
				else:
					print(f"[{Fore.YELLOW}-{Fore.RESET}] Unknown Error")
	except Exception as e:
		print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
	print(f"{Fore.GREEN} Finished!"+Fore.RESET)
	Start()

def Destroy(webhook):
	try:
		print(f"[{Fore.GREEN}+{Fore.RESET}] Spamming webhook...")
		if config["useproxy"] == True:
			proxy = proxy = random.choice(proxies)
			for _ in range(150):
				time.sleep(1)
				r = req.post(webhook, json = {'content':f'''{config["destroyspam"]}''','username':config["username"],'avatar_url':config["avatar"]}, proxies = proxy)
		else:
			for _ in range(150):
				time.sleep(1)
				r = req.post(webhook, json = {'content':f'''{config["destroyspam"]}''','username':config["username"],'avatar_url':config["avatar"]})
		print(f"{Fore.GREEN} Finished!"+Fore.RESET)
		print(f"[{Fore.GREEN}+{Fore.RESET}] Deleting webhook...")
		r = req.delete(webhook)
		print(f"{Fore.GREEN} Finished!"+Fore.RESET)
	except Exception as e:
		print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
	Start()

def Delete(webhook):
	try:
		r = req.delete(webhook)
		if r.status_code == 204:
			print(f"{Fore.GREEN} Webhook deleted!"+Fore.RESET)
		elif r.status_code == 404:
			print(f"[{Fore.YELLOW}-{Fore.RESET}] Invalid webhook")
		else:
			print(f"[{Fore.YELLOW}-{Fore.RESET}] Unknown Error | Status Code: {r.status_code}")
	except Exception as e:
		print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
	Start()

def GetInfo(webhook):
	try:
		r = req.get(webhook).json()
		wID = r["id"]
		wTOKEN = r["token"]
		wGUILD = r["guild_id"]
		wCHANNEL = r["channel_id"]
		print(f'''[{Fore.GREEN}Webhook ID{Fore.RESET}] {wID}
[{Fore.GREEN}Token{Fore.RESET}] {wTOKEN}
[{Fore.GREEN}Guild ID{Fore.RESET}] {wGUILD}
[{Fore.GREEN}Channel ID{Fore.RESET}] {wCHANNEL}''')
	except Exception as e:
		print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
	Start()

def Clear():
	os.system('cls')

def Start():
	command = list(input('').split(','))
	if command[0] == 'help':
		Help()
	if command[0] == 'scrape-proxies':
		Scrape()
	elif command[0] == 'clear':
		Clear()
		Menu()
		Start()
	elif command[0] == 'spam':
		webhook = command[1]
		message = command[2]
		amount = int(command[3])
		Spam(webhook, message, amount)
	elif command[0] == 'delete':
		webhook = command[1]
		Delete(webhook)
	elif command[0] == 'destroy':
		webhook = command[1]
		Destroy(webhook)
	elif command[0] == 'getinfo':
		webhook = command[1]
		GetInfo(webhook)
	else:
		print(f'{Fore.YELLOW}Invalid Command, type "help" for a list of valid commands.'+Fore.RESET)
		Start()

if __name__ == '__main__':
	try:
		Clear()
		Menu()
		Start()
	except Exception as e:
		print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
