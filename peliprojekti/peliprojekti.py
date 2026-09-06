# Tee kansioon ohjelma, joka kysyy pelaajan nimen ja iän, tallentaa nämä muuttujiin ja tulostaa konsoliin.

nimi = input("Nimi: \n")
ika = input("Ikä: \n")
komento = None

print("Nimesi on " + nimi)
print("Olet " + ika + " vuotias")

ika = float(ika)
if ika < 12:
    print('Olet liian nuori pelaamaan peliä.')
    quit()

while True:
    print('Komennot:\n1. Printtaa hymiö sanomalla hymiö.')
    print('2. Printtaa ikäsi sanomalla ikä.')
    print('3. Printtaa nimesi sanomalla nimi.')
    print('Voit lopettaa pelin sanomalla lopeta.')
    komento = input('Komento: ')

    if komento == "hymiö":
        print(":)")
    elif komento == "ikä":
        print(ika)
    elif komento == "nimi":
        print(nimi)
    elif komento == "lopeta":
        quit()