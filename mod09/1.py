class Auto:

    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 50
        self.kuljettu_matka = 100


print(f"Rekisteritunnus: {Auto.rekisteritunnus}")
print(f"Huippunopeus: {Auto.huippunopeus} km/h")
print(f"Tämänhetkinen nopeus: {Auto.tamanhetkinen_nopeus} km/h")
print(f"Kuljettu matka: {Auto.kuljettu_matka} km")