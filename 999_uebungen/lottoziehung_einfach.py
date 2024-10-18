"""
Lotto 6 aus 49

Schreibe ein Programm, das 6 unterschiedliche Zufallszahlen zwischen 1 und 49 zieht.

Gebe die Zahlen aus, sobald 6 unterschiedliche Zahlen vorhanden sind

"""
import random

# for i in range(10):
#     print(int(random.random() + 49 + 1)) #Output: Double/Float Zahl zwischen 0 und nicht 1

def rnd_ganzzahl(start, end):
    return int(random.random() * (end - start + 1) + start)


def rnd_boolean():
    return random.choice([True, False])
print (rnd_boolean())


rnd_wert = 1
while (rnd_wert != 49):
    rnd_wert = rnd_ganzzahl(1, 49)

for i in range(100):
    print(rnd_ganzzahl(1,49))

print ('Durch')
for i in range(10):
    print (rnd_boolean())