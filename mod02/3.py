kanta = input("Suorakulmion kanta (m): ")
korkeus = input ("Suorakulmion korkeus (m): ")

kanta, korkeus = float(kanta), float(korkeus)

print(f"Suorakulmion piiri: {2 * kanta + 2 * korkeus: .2f} metriä")
print(f"Suorakulmion pinta-ala: {kanta * korkeus: .2f} neliömetriä")