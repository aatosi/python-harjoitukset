print("Syötä kolme kokonaislukua!\n")

luku1 = input("Luku 1: ")
luku2 = input("Luku 2: ")
luku3 = input("Luku 3: ")

luku1, luku2, luku3 = int(luku1), int(luku2), int(luku3)

print(f"Lukujen summa: {luku1+luku2+luku3: .0f}")
print(f"Lukujen tulo: {luku1*luku2*luku3: .0f}")
print(f"Lukujen keskiarvo: {(luku1+luku2+luku3)/3: .2f}")