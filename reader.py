import json
import time
import os
from colorama import Fore, Style, init
init(convert=True)

def readermain():
    filer = open('coords.json', 'r', encoding='utf-8')
    json_data = json.load(filer)


    for data in json_data:
        print(Fore.GREEN + 'Name: '+ Fore.WHITE + str(data['name']) + Fore.GREEN +' Coords: '+Fore.RED+"Overworld "+ Fore.WHITE + str(data['coords']['overworld']) + f"; {Fore.RED}Nether "+ Fore.WHITE + str(data['coords']['nether']))
def fuckingyourmom():
    os.system('CLS')
    readermain()
    print(Fore.RED + '\n\nExit in 10s!')
    time.sleep(8)
    print(Fore.RED + 'Exit in 2s!')
    time.sleep(2)    
        