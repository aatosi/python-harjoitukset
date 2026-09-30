inventaario = []

def lisää_esine(lista):
    uusi_esine = input('Anna uusi esine: ')
    if uusi_esine:
        lista.append(uusi_esine)
        print(f'Inventaarioon lisätty {uusi_esine}.\n')
    else:
        print('Et syöttänyt esinettä.\n')

def listaa_esineet(lista):
    if not lista:
        print('Inventaario on tyhjä.\n')
    else:
        print('\n- Inventaario -')
        n = 0
        for i in lista:
            n += 1
            print(f'{n}. {i}')
        print('\n')

def näytä_tiedot(nimi, ikä):
    print(f'\n- Pelaajan tiedot -')
    print(f'Nimi: {nimi}')
    print(f'Ikä: {ikä}')
    print('\n')

nimi = input('Syötä nimesi: \n')
ikä_input = input('Syötä ikäsi: \n')

print(f'Nimesi on {nimi} ja olet {ikä_input} vuotias.')

try:
    ikä = int(ikä_input)
except ValueError:
    print('Virheellinen ikä, syötä kokonaisluku.')

if ikä < 12:
    print('Olet liian nuori pelaamaan peliä.')
    quit()

while True:
    print('Komennot:')
    print('1. Lisää esineitä sanomalla "esine"')
    print('2. Listaa omat esineet sanomalla "listaa"')
    print('3. Printtaa tietosi sanomalla "tiedot"')
    print('Voit lopettaa pelin sanomalla "lopeta"')

    komento = input('Komento: ')

    if komento == 'esine':
        lisää_esine(inventaario)
    elif komento == 'listaa':
        listaa_esineet(inventaario)
    elif komento == 'tiedot':
        näytä_tiedot(nimi, ikä)
    elif komento == 'lopeta':
        print('Kiitos pelaamisesta, peli lopetetaan.')
        break
    else:
        print('Tuntematon komento.')