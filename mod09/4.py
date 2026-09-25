import random


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


autot = []
for i in range(1, 11):
    autot.append(Auto(f"ABC-{i}", random.randint(100, 200)))

kilpailu_kaynnissa = True

while kilpailu_kaynnissa:
    for auto in autot:
        auto.kiihdyta(random.randint(-10, 15))
        auto.kulje(1)
        if auto.kuljettu_matka >= 10000:
            kilpailu_kaynnissa = False

print(
    f"{'Rekisteri':<12} | {'Huippunopeus (km/h)':<20} | {'Nopeus (km/h)':<15} | {'Matka (km)':<12}"
)
print("-" * 68)

for auto in autot:
    print(
        f"{auto.rekisteritunnus:<12} | {auto.huippunopeus:<20} | {auto.tamanhetkinen_nopeus:<15} | {auto.kuljettu_matka:<12.1f}"
    )