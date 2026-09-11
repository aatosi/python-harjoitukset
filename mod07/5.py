def eiparittomia(lista):
    karsittu = []

    for luku in lista:
        if luku % 2 == 0:
            karsittu.append(luku)

    return karsittu


luvut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

karsittu = eiparittomia(luvut)

print("Alkuperäinen lista:", luvut)
print("Karsittu lista:", karsittu)