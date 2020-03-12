import random


def randscore2():
    namelist = list()
    print("Type 'Quit' to stop")
    while True:
        name = input('Name: ')
        if name == 'Quit':
            break
        namelist.append(name)
    return namelist


for name in randscore2():
    score = random.randint(15, 35)
    print('{:10} - {:2}'.format(name, score))
