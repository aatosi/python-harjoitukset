class Auto:

    def __init__(self, rekisteritunnus, huippunopeus, nykynopeus, matka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nykynopeus = 0
        self.matka = 0

rekisteritunnus = "ABC-123"
huippunopeus = 142

# en osannut tehdä


print(f"Rekisteritunnus: {Auto.rekisteritunnus}")
print(f"Huippunopeus: {Auto.huippunopeus} km/h")
print(f"Tämänhetkinen nopeus: {Auto.nykynopeus} km/h")
print(f"Kuljettu matka: {Auto.matka} km")