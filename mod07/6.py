import math

def yksikkohinta(halkaisija, hinta):
    sade = halkaisija / 2 / 100
    pinta_ala = math.pi * sade ** 2
    return hinta / pinta_ala


halkaisija1 = float(input("Ensimmäisen pizzan halkaisija cm: "))
hinta1 = float(input("Ensimmäisen pizzan hinta euroina: "))

halkaisija2 = float(input("Toisen pizzan halkaisija cm: "))
hinta2 = float(input("Toisen pizzan hinta euroina: "))

hinta_m2_1 = yksikkohinta(halkaisija1, hinta1)
hinta_m2_2 = yksikkohinta(halkaisija2, hinta2)

if hinta_m2_1 < hinta_m2_2:
    print("Ensimmäisessä pizzassa on enemmän vastinetta rahalle.")
elif hinta_m2_2 < hinta_m2_1:
    print("Toisessa pizzassa on enemmän vastinetta rahalle.")
else:
    print("Pizzat ovat yhtä kannattavia ostaa.")