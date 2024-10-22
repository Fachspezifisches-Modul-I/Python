from random import randint


# Lottozahlen 6 unterschiedliche bei 6 Iterationen

# Trommel
lotto_trommel = list(range(1, 50))
ziehung = []


for i in range(6):
    rnd_zahl = randint(0, len(lotto_trommel)) # Zufallszahl zwischen 0 und der Länge der Liste
    gezogene_zahl = lotto_trommel.pop(rnd_zahl)
    ziehung.append(gezogene_zahl)

print(ziehung)
print (lotto_trommel)
