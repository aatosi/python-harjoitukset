import random

def heitä(tahkot):
    return random.randint(1, tahkot)

maksimi = int(input("Anna nopan maksimisilmäluku: "))

while True:
    silmaluku = heitä(maksimi)
    print(silmaluku)

    if silmaluku == maksimi:
        break