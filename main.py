import json

nukname = input("Write name: ")
overwX = input("Write Overworld cord X ")
overwY = input("Write Overworld cord Y ")
overwZ = input("Write Overworld cord Z ")

netherX = int(overwX)/8
netherY = int(overwY)
netherZ = int(overwZ)/8




def get():
    overworldOUT = (
        'X: ' + overwX,
        'Y: ' + overwY,
        'Z: ' + overwZ
    )
    netherOUT = (
        'X: ' + str(netherX),
        'Y: ' + str(netherY),
        'Z: ' + str(netherZ)
    )

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
        data = json.load(open('coords.txt'))
    except:
        data = []

    data.append(tabled)

    with open('coords.txt', 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

def main():

    for i in range(1):
        write_txt_json(get())


if __name__ == '__main__':
    main()

