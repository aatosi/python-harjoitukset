aluku = int(input("Anna kokonaisluku:\n"))
omaluku = True

if aluku < 2:
    omaluku = False
else:
    for lluku in range(2, aluku):
        if aluku % lluku == 0:
            omaluku = False
            break

if omaluku:
    print("Luku on alkuluku.")
else:
    print("Lukusi ei ole alkuluku.")