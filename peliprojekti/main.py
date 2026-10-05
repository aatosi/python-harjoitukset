import json
import os
from properties import Esine, Alue, Pelaaja

# Funktiot

def lue_tiedosto(tiedoston_nimi):
    try:
        with open(tiedoston_nimi, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return f'Tiedostoa {tiedoston_nimi} ei löytynyt.'


def listaa_esineet(pelaaja):
    if not pelaaja.esineet:
        print('\nEt ole vielä kerännyt roskia.\n')
    else:
        yhteispaino = sum(e.paino for e in pelaaja.esineet)
        print(f'\n--- Kerätyt roskat ({len(pelaaja.esineet)} kpl, yhteensä {yhteispaino:.2f} kg) ---')
        for i, e in enumerate(pelaaja.esineet, 1):
            print(f'{i}. {e.nimi} ({e.paino} kg)\n')
        print('---------------------------------------------------')


def näytä_tiedot(pelaaja, ikä, roskat_yhteensä):
    kerätty = len(pelaaja.esineet)
    print('\n--- Pelaajan tiedot ---')
    print(f'Nimi: {pelaaja.nimi}')
    print(f'Ikä: {ikä}')
    print(f'Sijainti: {pelaaja.sijainti.nimi}')
    print(f'Edistyminen: {kerätty}/{roskat_yhteensä} roskaa kerätty')
    print('-------------------------------\n')

def tallenna_peli(pelaaja, ikä, alueet):
    tiedoston_nimi = f'{pelaaja.nimi}_savedata.json'

    # Muunnetaan oliot dictionary muotoon
    data = {
        'pelaaja' : {
            'nimi' : pelaaja.nimi,
            'ikä' : ikä,
            'sijainti' : pelaaja.sijainti.nimi,
            'esineet' : [{'nimi' : e.nimi, 'paino' : e.paino} for e in pelaaja.esineet]
        },
        'alueet' : [
            {
                'nimi' : a.nimi,
                'kuvaus' : a.kuvaus,
                'esineet' : [{'nimi' : e.nimi, 'paino' : e.paino} for e in a.esineet]
            }
            for a in alueet
        ]

    }

    with open(tiedoston_nimi, 'w', encoding='utf-8') as f:
        json.dump(data, f)
    print(f'\nPelitilanne tallennettu tiedostoon: "{tiedoston_nimi}"')


# Alusetetaan roskat

pahvimuki = Esine('Kertakäyttöinen kahvimuki', 0.05)
muovipullo = Esine('Litistynyt muovipullo', 0.1)
tölkki = Esine('Tyhjä energiajuomatölkki', 0.05)
sipsipussi = Esine('Tyhjä sipsipussi', 0.02)
tupakantumppi = Esine('Tupakantumppi', 0.01)
rengas = Esine('Vanha polkupyörän rengas', 1.2)
pizzalaatikko = Esine('Rasvainen pizzalaatikko', 0.3)
lasinsiru = Esine('Rikkoutunut lasipullo', 0.4)
kertakäyttögrilli = Esine('Ruostunut kertakäyttögrilli', 0.8)

# Alustetaan alueet ja roskat
def luo_uusi_maailma():
    pahvimuki = Esine('Kertakäyttöinen kahvimuki', 0.05)
    muovipullo = Esine('Litistynyt muovipullo', 0.1)
    tölkki = Esine('Tyhjä energiajuomatölkki', 0.05)
    sipsipussi = Esine('Tyhjä sipsipussi', 0.02)
    tupakantumppi = Esine('Tupakantumppi', 0.01)
    rengas = Esine('Vanha polkupyörän rengas', 1.2)
    pizzalaatikko = Esine('Rasvainen pizzalaatikko', 0.3)
    lasinsiru = Esine('Rikkoutunut lasipullo', 0.4)
    kertakäyttögrilli = Esine('Ruostunut kertakäyttögrilli', 0.8)

    tori = Alue('Kauppatori', 'Vilkas torialue, jonka mukulakivillä tuuli pyörittää irtoroskia.',
                [pahvimuki, pizzalaatikko])
    rantapuisto = Alue('Rantapuisto',
                       'Kaunis puistoalue vesistön äärellä. Nurmikolle ja kaislikkoon on jätetty jätteitä.',
                       [lasinsiru, kertakäyttögrilli, muovipullo])
    pururata = Alue('Metsäpururata', 'Rauhallinen lenkkipolku metsän siimeksessä. Ojan pientareelta erottuu roskia.',
                    [rengas, tölkki])
    skeittiparkki = Alue('Skeittiparkki',
                         'Betoninen ramppialue, jonka reunoille iltahengailijat ovat jättäneet roskiansa.',
                         [sipsipussi, tölkki])
    bussiasema = Alue('Linja-autoasema', 'Bussipysäkkien ja katosten ympärillä on kasanpäin pienroskaa.',
                      [tupakantumppi, pahvimuki])

    return [tori, rantapuisto, pururata, skeittiparkki, bussiasema]


# Intro & Kyselyt

print('\nTervetuloa pelaamaan mahtavaa peliä - Roskaralli 3000!\n')
nimi = input('Syötä nimesi: \n')
tallennus_tiedosto = f'{nimi}_savedata.json'

if os.path.exists(tallennus_tiedosto):
    print(f'\nNimellä {nimi} löytyi tallennus! Ladataan peli...\n')
    with open(tallennus_tiedosto, 'r', encoding='utf-8') as f:
        data = json.load(f)

    alueet = []
    for a_data in data['alueet']:
        esineet = [Esine(e['nimi'], e['paino']) for e in a_data['esineet']]
        alueet.append(Alue(a_data['nimi'], a_data['kuvaus'], esineet))

    pelaaja_data = data['pelaaja']
    ikä = pelaaja_data['ikä']

    sijainti_alue = next((a for a in alueet if a.nimi == pelaaja_data['sijainti']), alueet[0])

    pelaaja = Pelaaja(pelaaja_data['nimi'], sijainti_alue)
    pelaaja.esineet = [Esine(e['nimi'], e['paino']) for e in pelaaja_data['esineet']]

else:
    ikä_input = input('Syötä ikäsi: \n')
    try:
        ikä = int(ikä_input)
    except ValueError:
        print('Virheellinen ikä, syötä kokonaisluku.')

    if ikä < 12:
        print('Olet liian nuori pelaamaan, peli suljetaan.')
        quit()

    alueet = luo_uusi_maailma()
    pelaaja = Pelaaja(nimi, alueet[0])

    print('\n' + lue_tiedosto('intro.txt'))

roskat_yhteensä = sum(len(a.esineet) for a in alueet) + len(pelaaja.esineet)

print(f'\nOn aika aloittaa työt, {pelaaja.nimi}!')
print(f'Aloitusalue: {pelaaja.sijainti.nimi} - {pelaaja.sijainti.kuvaus}')

# Pelin looppi

while True:
    # Tarkistetaan onko kaikki roskat kerätty:
    if len(pelaaja.esineet) == roskat_yhteensä:
        print('\n' + lue_tiedosto('outro.txt'))
        if os.path.exists(tallennus_tiedosto):
            os.remove(tallennus_tiedosto)
            print('\n\nPeli suoritettu loppuun, tallennustiedosto poistetaan.\nKiitos pelaamisesta!')
        break

    # Muu pelin loop jos roskia jäljellä:

    print('Komennot:')
    print('1. Kerää roskia sanomalla "kerää"')
    print('2. Liiku toiselle alueelle sanomalla "liiku"')
    print('3. Listaa kerätyt roskat sanomalla "listaa"')
    print('4. Näytä tiedot sanomalla "tiedot"')
    print('5. Näytä pelin ohjeet sanomalla "ohjeet"')
    print('Voit lopettaa pelin ja tallentaa tiedot sanomalla "lopeta"')

    komento = input('Komento: ')

    if komento == 'kerää':
        pelaaja.keraa_esine()

    elif komento == 'liiku':
        print('\nValitse alue:')
        for i, a in enumerate(alueet, 1):
            print(f'{i}. {a.nimi}')

        valinta = input('Syötä alueen nimi tai numero: ')
        löytyi = False

        if valinta.isdigit():
            idx = int(valinta) - 1
            if 0 <= idx < len(alueet):
                pelaaja.liiku(alueet[idx])
                löytyi = True
        else:
            for a in alueet:
                if a.nimi == valinta:
                    pelaaja.liiku(a)
                    löytyi = True
                    break

        if not löytyi:
            print('Aluetta ei löydy.')

    elif komento == 'listaa':
        listaa_esineet(pelaaja)

    elif komento == 'tiedot':
        näytä_tiedot(pelaaja, ikä, roskat_yhteensä)

    elif komento == 'ohjeet':
        print('\n' + lue_tiedosto('ohjeet.txt') + '\n')

    elif komento == 'lopeta':
        tallenna_peli(pelaaja, ikä, alueet)
        print('Tallennetaan ja suljetaan peli. Kiitos pelaamisesta!')
        break

    else:
        print('Komentoa ei löydy.\n')

