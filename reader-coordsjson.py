import json
from colorama import Fore, Style, init
init(convert=True)
filer = open('coords.json', 'r', encoding='utf-8')
json_data = json.load(filer)


for data in json_data:
    print(Fore.GREEN + 'Name: '+ Fore.WHITE + str(data['name']) + Fore.GREEN +' Coords: ' + Fore.WHITE + str(data['coords']))
