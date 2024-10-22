# Gewinnlkassenermittlung vie Berechnung

## Code der Methode



def gewinnklasse_sz(richtige, richtige_sz):
#Range sichern
    if richtige < 2 or richtige > 6 or (richtige == 2 and not richtige_sz):
        return
    return 14 - 2 * richtige - richtige_sz

print(gewinnklasse_sz(3, True))
