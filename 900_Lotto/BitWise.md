# Lottoziehungen in binärer Struktur speichern

## Scratch Book

### Erste Betrachtung

* Es gibt 6 Plätze für die Lottoziehung
* Die Werte von 1 bis 49 sind mit n = n + 1 vertreten
* Es sind also 49 unterschiedliche Zahlen einer Raihe
* Zusätzlich gibt es die Superzahl (0 - 9)

Eine vollständige Darstellung aller gezogenen Zahlen bedarf inklusive der Superzahl:

* 6 Zahlen aus dem Bereich von 1 bis 49
* Eine Zahl im Bereich zwischen 0 und 9

#### Aufteilung in Koordinatensystem

2-dimensionale Matrix 7 x 7. Indizes von 0 bis 6  
49-Bit für 1 bis 49. 0b1 -> gesetzt an Position n
4 Bit für 0 bis 9.

Beispiel für

12, 21, 25, 36, 43, 49
Superzahl 7

Ob00000000000100000000100010000000000100000010000010111

53-bit je Ziehung

Eigenen Tipp xor Ziehung. 0 ist 6SZ

## Mit Vektoren

Koordinaten der richtigen Speichern. Damit benötige ich 6 Bit je Zahl. 
Also 6 * 6 Bit -> 36 Bit -> + 4 Bit für die Superzahl -> 40 Bit.
Der Bedarf je Reihe ist 13 bit geringer. Damit 25% weniger Speicherauslastung

12, 21, 25, 36, 43, 49
Superzahl 7

(x/y)
(0/0) -> 1
(0/1) -> 8
(2/2) -> 17
...

```py
def dec_2_coord_7x7(dec_value):
    x = (dec_value - 1) % 7
    y = (dec_value - 1) // 7

def coord_2_dec_7x7(x, y):
    pass
```
