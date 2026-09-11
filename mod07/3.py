def gallona(gallonat):
    return gallonat * 3.785

while True:
    gallonat = float(input("Anna gallonamäärä: "))

    if gallonat < 0:
        break

    litrat = gallona(gallonat)
    print("Litroja:", litrat)