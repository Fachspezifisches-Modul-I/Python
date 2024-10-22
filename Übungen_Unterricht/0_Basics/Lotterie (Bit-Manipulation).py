import random
from collections import Counter

def set_bit(number, bit_position):
    """Setzt das Bit an der angegebenen Position."""
    return number | (1 << (bit_position - 1))

def is_bit_set(number, bit_position):
    """Überprüft, ob das Bit an der angegebenen Position gesetzt ist."""
    return (number >> (bit_position - 1)) & 1

def random_lotto_zahlen():
    zahlen_bitmask = 0
    while bin(zahlen_bitmask).count('1') < 6:
        zahl = random.randint(1, 49)
        zahlen_bitmask = set_bit(zahlen_bitmask, zahl)
    return zahlen_bitmask

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
    # Generiere zufällige Nutzertipps als Bitmaske
    nutzer_zahlen_bitmask = random_lotto_zahlen()
    nutzer_superzahl = random.randint(0, 9)

    print(f"Zufällige Nutzertipps: Bitmaske: {bin(nutzer_zahlen_bitmask)}, Superzahl: {nutzer_superzahl}")

    ziehungen = 0
    gewinn_haeufigkeit = Counter()

    while True:
        ziehungen += 1

        # Ziehung der Lottozahlen und Superzahl als Bitmaske
        lotto_zahlen_bitmask = random_lotto_zahlen()
        lotto_superzahl = random.randint(0, 9)

        # Anzahl der gemeinsamen gesetzten Bits (Richtige Zahlen)
        gemeinsame_zahlen_bitmask = nutzer_zahlen_bitmask & lotto_zahlen_bitmask
        gemeinsame_zahlen = bin(gemeinsame_zahlen_bitmask).count('1')
        superzahl_richtig = (nutzer_superzahl == lotto_superzahl)

        # Bestimme die Gewinnklasse
        klasse = gewinnklasse(gemeinsame_zahlen, superzahl_richtig)

        # Ausgabe der Ziehung
        print(f"Ziehung {ziehungen}: Bitmaske: {bin(lotto_zahlen_bitmask)}, Superzahl: {lotto_superzahl}")

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
