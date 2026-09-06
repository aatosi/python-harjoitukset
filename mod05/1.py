import random

arvat = int(input("Anna arpakuutioiden määrä: "))
summa = 0

for maara in range(arvat):
    luku = random.randint(1, 6)
    summa += luku

print(f"Tässä summa arpakuutioista: {summa}")