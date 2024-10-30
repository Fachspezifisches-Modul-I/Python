def berechne_dm_in_euro(dm_betrag, umrechnungskurs=1.95583):
    euro_betrag = dm_betrag / umrechnungskurs
    return round(euro_betrag, 2)

def berechne_euro_in_dm(euro_betrag, umrechnungskurs=1.95583):
    dm_betrag = euro_betrag * umrechnungskurs
    return round(dm_betrag, 2)

def währungsumrechner():
    währung = input("Möchten Sie von DM zu Euro oder von Euro zu DM umrechnen? (Geben Sie 'DM' oder 'Euro' ein): ")
    betrag = input("Geben Sie den Betrag ein: ")

    # Eingabe bereinigen
    betrag = betrag.replace(",", ".")  # Ersetzt Kommas durch Punkte
    betrag = ''.join(filter(lambda x: x.isdigit() or x == '.', betrag))  # Entfernt alle Nicht-Ziffern (außer dem Punkt)

    try:
        betrag = float(betrag)
        if währung.lower() == 'dm':
            ergebnis = berechne_dm_in_euro(betrag)
            print(f"{betrag} DM entspricht {ergebnis} €")
        elif währung.lower() == 'euro':
            ergebnis = berechne_euro_in_dm(betrag)
            print(f"{betrag} € entspricht {ergebnis} DM")
        else:
            print("Ungültige Eingabe. Bitte geben Sie 'DM' oder 'Euro' ein.")
    except ValueError:
        print("Fehlerhafte Eingabe. Bitte geben Sie eine gültige Zahl ein.")

# Aufruf der Funktion
währungsumrechner()
