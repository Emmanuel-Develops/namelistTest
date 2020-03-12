import random
# EDS practical animation score generation program

def randscore2():
    namelist = list([])
    print("Type 'Quit' to stop")
    name = input('Name: ')
    while name != "Quit":
        score = random.randint(15, 35)
        namelist.append([name + ' - ' + str(score)])
        name = input('Name: ')
    return namelist


print(randscore2())
