numerot = []

while True:
    kysmys = input("Anna numero: ")
    if kysmys == "":
        break
    numerot.append(int(kysmys))

numerot.sort(reverse=True)


for luku in numerot[:5]:
    print(luku)