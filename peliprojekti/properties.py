class Esine:
    def __init__(self, nimi, paino):
        self.nimi = nimi
        self.paino = paino

class Huone:
    def __init__(self, nimi, esine: Esine):
        self.nimi = nimi
        self.esine = esine

class Pelaaja:
    def __init__(self, nimi, sijainti: Huone):
        self.nimi = nimi
        self.esineet = []
        self.sijainti = sijainti

    def liiku(self, kohde: Huone):
        self.sijainti = kohde
        print(f'Liikuit huoneeseen {kohde.nimi}.\n')

    def kerää_esine(self):
        if self.sijainti.esine is not None:
            kerätty = self.sijainti.esine
            self.esineet.append(kerätty)
            self.sijainti.esine = None
            print(f'Kerösit esineen {kerätty.nimi}, paino {kerätty.paino}kg.\n')
        else:
            print('Tässä huoneessa ei ole esineitä.\n')