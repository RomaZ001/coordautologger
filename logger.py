import json
import time
from colorama import Style, Fore, init
from reader import fuckingyourmom
import os

filename = 'coords.json'

init(convert=True)
os.system('CLS')
print('Select option')
print('[1] Logger')
print('[2] Checker')
optionSet=input('Option?: ')
if optionSet=='1':
    os.system('CLS')
    nukname = input("Write name: ")
    os.system('CLS')
    print('Write a coord world \n')
    print('[1] Overworld')
    print('[2] Nether')
    typecoord=input('Option?: ')
    os.system('CLS')
if optionSet=='2':
    os.system('CLS')
    fuckingyourmom()
    exit()

if typecoord=='1':
    overwX = input("Write Pos X ")
    os.system('CLS')
    overwY = input("Write Pos Y ")
    os.system('CLS')
    overwZ = input("Write Pos Z ")
    os.system('CLS')

    overworldOUT = (
        'X: ' + str(overwX),
        'Y: ' + str(overwY),
        'Z: ' + str(overwZ)
    )

    netherXdel8 = int(overwX)//8
    netherYdel8 = int(overwY)
    netherZdel8 = int(overwZ)//8

    netherOUT = (
        'X: ' + str(netherXdel8),
        'Y: ' + str(netherYdel8),
        'Z: ' + str(netherZdel8)
    )


if typecoord=='2':
    netherX = input("Write! Pos X ")
    os.system('CLS')
    netherY = input("Write! Pos Y ")
    os.system('CLS')
    netherZ = input("Write! Pos Z ")
    os.system('CLS')


    netherOUT = (
        'X: ' + str(netherX),
        'Y: ' + str(netherY),
        'Z: ' + str(netherZ)
    )

    overwXdel8 = int(netherX)*8
    overwYdel8 = int(netherY)
    overwZdel8 = int(netherZ)*8
    
    overworldOUT = (
        'X: ' + str(overwXdel8),
        'Y: ' + str(overwYdel8),
        'Z: ' + str(overwZdel8)
    )


def get():
    coords = {'overworld': overworldOUT,
              'nether': netherOUT
             }



    using = {
        'name': nukname,
        'coords': coords
    }
    return using

def write_txt_json(tabled):
    try:
        data = json.load(open(filename))
    except:
        data = []

    data.append(tabled)

    with open(filename, 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

def main():
    for i in range(1):
        write_txt_json(get())
    print('Okay. i finished!, saved in ' + filename)
    print(Fore.RED + '\nExit in 10s!')
    time.sleep(1)
    print(Fore.RED + 'Exit in 9s!')
    time.sleep(1)
    print(Fore.RED + 'Exit in 8s!')
    time.sleep(1)
    print(Fore.RED + 'Exit in 7s!')
    time.sleep(1)
    print(Fore.RED + 'Exit in 6s!')
    time.sleep(1)
    print(Fore.RED + 'Exit in 5s!')
    time.sleep(1)
    print(Fore.RED + 'Exit in 4s!')
    time.sleep(1)
    print(Fore.RED + 'Exit in 3s!')
    time.sleep(1)
    print(Fore.RED + 'Exit in 2s!')
    time.sleep(1)
    print(Fore.RED + 'Exit in 1s!')
    time.sleep(1)


if __name__ == '__main__':
    main()

