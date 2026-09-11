value = None
isoin = None
pienin = None

print('\nVoit lopettaa ohjelman syöttämällä tyhjän merkkijonon vastauksena.\n')

while True:
    value = input('Syötä luku: ')

    if value == "":
        break

    value = float(value)
    if isoin is None or value > isoin:
        isoin = value
    elif pienin is None or value < pienin:
        pienin = value



print(f'Suurin luku oli {isoin: .2f} ja pienin {pienin: .2f}')