from random import randint

liste = []

for i in range(1000):
    erg = 0
    for wuerfe in range(5):
        erg += randint(1, 6)

    liste.append(erg)

for augen in range(5, 31):
    anzahl = 0
    for element in liste:
        if augen == element:
            anzahl += 1

    xstr = ''
    for j in range(anzahl):
        xstr += "x"

    print(f"{augen}->{xstr}")
