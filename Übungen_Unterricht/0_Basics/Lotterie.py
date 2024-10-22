import random
from collections import Counter
import gc

def ziehung():
    zahlen = random.sample(range(1, 50), 6)
    zahlen.sort()
    superzahl = random.randint(0, 9)
    return zahlen, superzahl

def gewinnklasse(anzahl_richtige, superzahl_richtig):
    if anzahl_richtige == 6:
        return 1 if superzahl_richtig else 2
    elif anzahl_richtige == 5:
        return 3 if superzahl_richtig else 4
    elif anzahl_richtige == 4:
        return 5 if superzahl_richtig else 6
    elif anzahl_richtige == 3:
        return 7 if superzahl_richtig else 8
    elif anzahl_richtige == 2 and superzahl_richtig:
        return 9
    return None


def lotto_simulation():
    nutzer_zahlen = random.sample(range(1, 50), 6)
    nutzer_zahlen.sort()
    nutzer_superzahl = random.randint(0, 9)

    print(f"Zufällige Nutzertipps: Zahlen: {nutzer_zahlen}, Superzahl: {nutzer_superzahl}")

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

        # Speicher optimieren
        del lotto_zahlen, lotto_superzahl, gemeinsame_zahlen, superzahl_richtig
        gc.collect()

    # Bonusausgabe
    print("\nGewinnhäufigkeit:")
    for klasse, haeufigkeit in sorted(gewinn_haeufigkeit.items()):
        print(f"Gewinnklasse {klasse}: {haeufigkeit} Mal gezogen")

# Starte die Simulation
lotto_simulation()
