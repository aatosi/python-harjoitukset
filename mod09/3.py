class Auto:

    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, nopeuden_muutos):
        uusi_nopeus = self.tamanhetkinen_nopeus + nopeuden_muutos
        if uusi_nopeus > self.huippunopeus:
            self.tamanhetkinen_nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.tamanhetkinen_nopeus = 0
        else:
            self.tamanhetkinen_nopeus = uusi_nopeus

    def kulje(self, tuntimaara):
        self.kuljettu_matka += self.tamanhetkinen_nopeus * tuntimaara


uusi_auto = Auto("ABC-123", 142)
uusi_auto.kuljettu_matka = 2000
uusi_auto.tamanhetkinen_nopeus = 60

uusi_auto.kulje(1.5)
print(f"Uusi kuljettu matka: {uusi_auto.kuljettu_matka} km")