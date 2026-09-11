sukupuoli = input("Anna biologinen sukupuolesi (nainen/mies): ")
arvo = int(input("Anna hemoglobiiniarvosi (g/l): "))

if sukupuoli == "nainen":
    if arvo < 117:
        print("Hemoglobiiniarvosi on alhainen.")
    elif arvo > 175:
        print("Hemoglobiiniarvosi on korkea.")
    else:
        print("Hemoglobiiniarvosi on normaali.")
elif sukupuoli == "mies":
    if arvo < 134:
        print("Hemoglobiiniarvosi on alhainen.")
    elif arvo > 195:
        print("Hemoglobiiniarvosi on korkea.")
    else:
        print("Hemoglobiiniarvosi on normaali.")
else:
    print("Tuntematon sukupuoli.")