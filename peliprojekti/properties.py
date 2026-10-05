class Esine:
    def __init__(self, nimi: str, paino: float):
        self.nimi = nimi
        self.paino = paino


class Alue:
    def __init__(self, nimi: str, kuvaus: str, esineet: list):
        self.nimi = nimi
        self.kuvaus = kuvaus
        self.esineet = esineet


class Pelaaja:
    def __init__(self, nimi: str, sijainti: Alue):
        self.nimi = nimi
        self.esineet = []
        self.sijainti = sijainti

    def liiku(self, kohde: Alue):
        self.sijainti = kohde
        print(f'\nLiikuit alueelle: {kohde.nimi}')
        print(f'{kohde.kuvaus}\n')

    def keraa_esine(self):
        if not self.sijainti.esineet:
            print('Tällä alueella ei ole enää roskia!\n')
            return

        print('\nAlueella olevat roskat:')
        for idx, esine in enumerate(self.sijainti.esineet, 1):
            print(f'{idx}. {esine.nimi} ({esine.paino} kg)')

        valinta = input('\nMinkä roskan haluat kerätä: ')

        valittu = None
        if valinta.isdigit():
            idx = int(valinta) - 1
            if 0 <= idx < len(self.sijainti.esineet):
                valittu = self.sijainti.esineet[idx]
        else:
            for esine in self.sijainti.esineet:
                if esine.nimi == valinta:
                    valittu = esine
                    break

        if valittu:
            self.esineet.append(valittu)
            self.sijainti.esineet.remove(valittu)
            print(f'\nPoimit roskan: {valittu.nimi} ({valittu.paino} kg)\n')
        else:
            print('Roskaa ei löytynyt.\n')