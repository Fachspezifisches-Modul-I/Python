"""
Schreibe ein Programm, mit dem Du Lotto spielen kannst. 6 aus 49.
 
Als Eingabe müssen 6 unterschiedliche Zahlen zwischen 1 und 49 aufgenommen werden. Als siebte Zahl erfolgt dann die Angabe der Superzahl (0 - 9)
 
In einer danach folgenden Schleife sollen per Zufallsgenerator ebenso 6 unterschiedliche(!) Zahlen gezogen und eine Superzahl ermittelt werden. Eine count Variable soll die Anzahl der insgesamten Durchläufe anzeigen.
 
Jede Gewinnkombination soll auf der Konsole ausgegeben werden.
 
Die Schleife ist fertig, wenn 6 Richtige inkl. Superzahl gezogen wurden. Dann die Gewinnkombination ausgeben und die Anzahl der Ziehungen.


Gewinnklassen (Die Ziffer ist die Anzahl der Richtigen. SZ ist die Superzahl)

I    -> 6SZ
II   -> 6
III  -> 5SZ
IV   -> 5
V    -> 4SZ
VI   -> 4
VII  -> 3SZ
VIII -> 3
IX   -> 2SZ   


Bonusmission:
Am Ende des kompletten Durchlaufes soll auch ausgegeben werden, wie oft welche Gewinnkombination gezogen wurde.

"""
# 0 -> 14
# 1 -> 12
# 2 -> 10
# 3 -> 8
# 4 -> 6
# 5 -> 4
# 6 -> 2
""" def gewinnklasse(richtige):
# Range sichern
    if richtige < 2 or richtige > 6:
        return
    return 14 - 2 * richtige

print(gewinnklasse(4)) """

# Nun müssen wir in diese Betrachtung Uch die Superzahl (SZ) einbeziehen

# Anzahl richtige steht in der Variable 'richtige' und ob die Superzahl
# getroffen wurde als Booleanwert in 'richtige_sz'
def gewinnklasse_sz(richtige, richtige_sz):
# Range sichern
    if richtige < 2 or richtige > 6 or (richtige == 2 and not richtige_sz):
        return
    return 14 - 2 * richtige - richtige_sz

print(gewinnklasse_sz(3, True))




