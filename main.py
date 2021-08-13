import json
from colorama import Style, Fore, init
init(convert=True)

nukname = input("Write name: ")
print('Write a coord world \n')
print('[1] Overworld')
print('[2] Nether')
typecoord=input()
if typecoord=='1':
    overwX = input("Write Pos X ")
    overwY = input("Write Pos Y ")
    overwZ = input("Write Pos Z ")

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
    netherY = input("Write! Pos Y ")
    netherZ = input("Write! Pos Z ")

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
        data = json.load(open('coords.json'))
    except:
        data = []

    data.append(tabled)

    with open('coords.json', 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

def main():
    for i in range(1):
        write_txt_json(get())
if __name__ == '__main__':
    main()

