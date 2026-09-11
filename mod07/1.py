import random

def heitto():
    return random.randint(1, 6)

while True:
    silmaluku = heitto()
    print(silmaluku)

    if silmaluku == 6:
        break