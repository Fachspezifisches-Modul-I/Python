import random
from collections import Counter

def ziehung():
    # Ziehe 6 unterschiedliche Zahlen zwischen 1 und 49 und eine Superzahl zwischen 0 und 9
    zahlen = random.sample(range(1, 50), 6)
    zahlen.sort()
    superzahl = random.randint(0, 9)
    return zahlen, superzahl

def gewinnklasse(anzahl_richtige, superzahl_richtig):
    if anzahl_richtige == 6 and superzahl_richtig:
        return 1
    elif anzahl_richtige == 6:
        return 2
    elif anzahl_richtige == 5 and superzahl_richtig:
        return 3
    elif anzahl_richtige == 5:
        return 4
    elif anzahl_richtige == 4 and superzahl_richtig:
        return 5
    elif anzahl_richtige == 4:
        return 6
    elif anzahl_richtige == 3 and superzahl_richtig:
        return 7
    elif anzahl_richtige == 3:
        return 8
    elif anzahl_richtige == 2 and superzahl_richtig:
        return 9
    return None

def lotto_simulation():
    # Generiere zufällige Nutzertipps
    nutzer_zahlen = random.sample(range(1, 50), 6)
    nutzer_zahlen.sort()
    nutzer_superzahl = random.randint(0, 9)

    print(f"Zufällige Nutzertipps: Zahlen: {nutzer_zahlen}, Superzahl: {nutzer_superzahl}")

    # Zählvariablen
    ziehungen = 0
    gewinn_haeufigkeit = Counter()

    while True:
        ziehungen += 1
        lotto_zahlen, lotto_superzahl = ziehung()
        gemeinsame_zahlen = len(set(nutzer_zahlen).intersection(lotto_zahlen))
        superzahl_richtig = (nutzer_superzahl == lotto_superzahl)
        klasse = gewinnklasse(gemeinsame_zahlen, superzahl_richtig)

        # Ausgabe der Ziehung
        print(f"Ziehung {ziehungen}: Zahlen: {lotto_zahlen}, Superzahl: {lotto_superzahl}")

        if klasse:
            gewinn_haeufigkeit[klasse] += 1
            print(f"Gewinnklasse erreicht: {klasse}")

            if klasse == 1:
                print(f"Jackpot! Du hast die höchste Gewinnklasse in {ziehungen} Ziehungen erreicht!")
                break

    # Bonusausgabe
    print("\nGewinnhäufigkeit:")
    for klasse, haeufigkeit in sorted(gewinn_haeufigkeit.items()):
        print(f"Gewinnklasse {klasse}: {haeufigkeit} Mal gezogen")

# Starte die Simulation
lotto_simulation()
