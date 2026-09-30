from properties import Esine, Huone, Pelaaja

# Funktiot

def listaa_esineet(pelaaja):
    if not pelaaja.esineet:
        print('Inventaario on tyhjä.\n')
    else:
        print('\n- Inventaario -')
        n = 0
        for e in pelaaja.esineet:
            n += 1
            print(f'{n}. {e.nimi}, ({e.paino}kg)')
        print('\n')

def näytä_tiedot(pelaaja, ikä):
    print(f'\n- Pelaajan tiedot -')
    print(f'Nimi: {pelaaja.nimi}')
    print(f'Ikä: {ikä}')
    print(f'Sijainti: {pelaaja.sijainti.nimi}')
    print('\n')

# Huoneiden / esineiden tilanne

miekka = Esine('Miekka', 2)
avain = Esine('Avain', 0.2)
kilpi = Esine('Kilpi', 1.5)
kahvikuppi = Esine('Kahvikuppi', 0.3)

olohuone = Huone('Olohuone', miekka)
eteinen = Huone('Eteinen', avain)
makuuhuone = Huone('Makuuhuone', kilpi)
keittiö = Huone('Keittiö', kahvikuppi)

huoneet = [olohuone, eteinen, makuuhuone, keittiö]


# Nimi / ikä kyselyt / intro

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

# Pelin looppi

pelaaja = Pelaaja(nimi, olohuone)

while True:
    print('Komennot:')
    print('1. Kerää esine sanomalla "kerää"')
    print('2. Liiku toiseen huoneeseen sanomalla "liiku"')
    print('3. Listaa omat esineet sanomalla "listaa"')
    print('4. Printtaa tietosi sanomalla "tiedot"')
    print('Voit lopettaa pelin sanomalla "lopeta"')

    komento = input('Komento: ')

    if komento == 'kerää':
        pelaaja.kerää_esine()

    elif komento == 'liiku':
        print('Valitse huoneista:\n')
        for i, h in enumerate(huoneet, 1):
            print(f'{i}. {h.nimi}')

        valinta = input('Mihin huoneeseen liikut? Syötä huoneen nimi: ')
        löytyi = False
        for h in huoneet:
            if h.nimi == valinta:
                pelaaja.liiku(h)
                löytyi = True
                break
        if not löytyi:
            print('Tuntematon huone.\n')

    elif komento == 'listaa':
        listaa_esineet(pelaaja)

    elif komento == 'tiedot':
        näytä_tiedot(pelaaja, ikä)

    elif komento == 'lopeta':
        print('Kiitos pelaamisesta, peli lopetetaan.')
        break

    else:
        print('Tuntematon komento.')