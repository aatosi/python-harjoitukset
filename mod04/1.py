pituus = int(input("Anna kuhan pituus senttimetreinä: "))
alamitta = 37

if pituus < alamitta:
    puuttuu = alamitta - pituus
    print(f"Kuhasi on alamittainen. Laske se takaisin järveen! Mitasta puuttuu vielä {puuttuu} cm.")
else:
    print("Hieno kala! Kuhan mitta on sallittu.")