def summa(lista):
    tulos = 0

    for luku in lista:
        tulos += luku

    return tulos

luvut = [5, 3, 2, 10]

summaus = summa(luvut)

print("Lukujen summa:", summaus)