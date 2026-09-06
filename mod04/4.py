import random

luku = random.randint(1, 10)
arvaus = None

while True:
    arvaus = float(input('Arvaa luku väliltä 1-10: '))

    if arvaus < luku:
        print('Liian pieni arvaus')
    elif arvaus > luku:
        print('Liian suuri arvaus')

    if arvaus == luku:
        print('Oikein!')
        break